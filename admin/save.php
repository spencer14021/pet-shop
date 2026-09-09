<?php
/**
 * Dr. Dobby — сохранение акций из панели /admin/ в assets/promos.json
 *
 * УСТАНОВКА: впишите свой пароль в строке PASSWORD ниже и загрузите папку
 * admin/ на хостинг вместе с сайтом. Больше ничего менять не нужно — файл
 * находит promos.json относительно самого себя, поэтому сайт можно
 * перенести на другой домен или в подпапку, и панель продолжит работать.
 *
 * Если на хостинге нет PHP, этот файл просто не запустится: панель заметит
 * это сама и предложит скачать promos.json и загрузить его файловым
 * менеджером. Ничего не сломается.
 */
/**
 * Пароль панели. Задаётся одним из двух способов:
 *
 *   1. Файл admin/password.php рядом с этим — одна строка:
 *          <?php return 'ваш-пароль';
 *      Так лучше: этот файл не попадает в репозиторий, и пароль не уезжает
 *      вместе с кодом никуда.
 *   2. Или прямо здесь, в строке ниже, если файлы кладутся руками по FTP.
 *
 * Пока пароль остался значением по умолчанию, запись запрещена.
 */
$PASSWORD = 'ЗАМЕНИТЕ-ЭТОТ-ПАРОЛЬ';
$secret = __DIR__ . '/password.php';
if (is_file($secret)) {
    $fromFile = require $secret;
    if (is_string($fromFile) && trim($fromFile) !== '') {
        $PASSWORD = trim($fromFile);
    }
}

/** Куда пишем. Путь считается от этого файла, а не от домена. */
$target = __DIR__ . '/../assets/promos.json';
$backup = __DIR__ . '/../assets/promos.backup.json';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

/** Ответ и выход — одним движением. */
function out($code, array $body) {
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

$configured = $PASSWORD !== 'ЗАМЕНИТЕ-ЭТОТ-ПАРОЛЬ';

/* Панель спрашивает об этом при открытии: есть ли тут PHP, задан ли пароль
   и может ли он вообще писать в assets/. Пароль для проверки не нужен —
   ничего секретного в ответе нет. */
if (isset($_GET['ping'])) {
    out(200, [
        'ok'         => true,
        'configured' => $configured,
        'writable'   => is_writable(file_exists($target) ? $target : dirname($target)),
    ]);
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    out(405, ['ok' => false, 'error' => 'Ожидается POST.']);
}

$raw = file_get_contents('php://input');
if ($raw === false || $raw === '') {
    out(400, ['ok' => false, 'error' => 'Пустой запрос.']);
}
if (strlen($raw) > 512 * 1024) {
    out(413, ['ok' => false, 'error' => 'Слишком большой файл: акции — это текст, не картинки.']);
}

$in = json_decode($raw, true);
if (!is_array($in)) {
    out(400, ['ok' => false, 'error' => 'Не удалось прочитать запрос.']);
}

if (!$configured) {
    out(403, ['ok' => false, 'error' => 'Пароль не задан. Создайте admin/password.php с вашим паролем или впишите его в admin/save.php.']);
}

/* Сравнение фиксированной длины: обычное === выходит на первом же несовпавшем
   символе, и по времени ответа пароль можно подобрать по одной букве. */
if (!is_string($in['password'] ?? null) || !hash_equals($PASSWORD, $in['password'])) {
    sleep(1);                                  // подбор паролем — не бесплатно
    out(403, ['ok' => false, 'error' => 'Неверный пароль.']);
}

/* Пишем только то, что панель и умеет читать: настройки и список акций.
   Всё остальное из запроса отбрасывается, чтобы в promos.json не появилось
   лишнего, если запрос придёт не из панели. */
$doc = $in['doc'] ?? null;
if (!is_array($doc) || !isset($doc['promos']) || !is_array($doc['promos'])) {
    out(400, ['ok' => false, 'error' => 'В запросе нет списка акций.']);
}

$clean = ['promos' => []];

$text_keys = ['tag', 'title', 'body', 'cta'];
foreach ($doc['promos'] as $i => $p) {
    if (!is_array($p)) continue;
    $one = [
        'id'     => (string)($p['id'] ?? ('promo-' . ($i + 1))),
        'active' => !empty($p['active']),
        'from'   => (string)($p['from'] ?? ''),
        'to'     => (string)($p['to'] ?? ''),
        'link'   => (string)($p['link'] ?? ''),
        'text'   => [],
    ];
    /* Отпечаток текста, с которого панель переводила: по нему она отличает
       свой перевод от написанного руками. Ни сайт, ни человек его не видят. */
    if (is_array($p['mt'] ?? null)) {
        foreach (['ru', 'en', 'es'] as $lang) {
            if (!empty($p['mt'][$lang])) {
                $one['mt'][$lang] = substr((string)$p['mt'][$lang], 0, 32);
            }
        }
    }
    foreach (['ru', 'en', 'es'] as $lang) {
        $t = is_array($p['text'][$lang] ?? null) ? $p['text'][$lang] : [];
        foreach ($text_keys as $k) {
            $one['text'][$lang][$k] = trim((string)($t[$k] ?? ''));
        }
    }
    $clean['promos'][] = $one;
}

$json = json_encode(
    $clean,
    JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);
if ($json === false) {
    out(500, ['ok' => false, 'error' => 'Не удалось собрать файл.']);
}

/* Предыдущая версия остаётся рядом: если акцию удалили по ошибке, её можно
   достать из promos.backup.json файловым менеджером. */
if (is_file($target)) {
    @copy($target, $backup);
}

/* Пишем во временный файл и переименовываем: посетитель, который в этот
   момент открывает сайт, получает либо старый файл целиком, либо новый —
   но никогда половину. */
$tmp = $target . '.tmp';
if (file_put_contents($tmp, $json . "\n", LOCK_EX) === false || !rename($tmp, $target)) {
    @unlink($tmp);
    out(500, ['ok' => false, 'error' => 'Нет прав на запись в assets/. Разрешите запись в assets/promos.json (обычно права 664).']);
}

out(200, ['ok' => true, 'count' => count($clean['promos'])]);
