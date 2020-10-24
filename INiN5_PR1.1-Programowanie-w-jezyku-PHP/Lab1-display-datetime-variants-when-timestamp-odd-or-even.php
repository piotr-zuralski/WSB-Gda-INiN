<?php

$dateTime = new DateTime();
$dateTime->setTimeZone(
    new DateTimeZone(
        date_default_timezone_get() ?: 'Europe/Warsaw'
    )
);
$tag = '<em>';
if ($dateTime->getTimestamp() % 2) {
    $tag = '<strong>';
}

$intlDate = null;
if (class_exists('IntlDateFormatter')) {
    \Locale::setDefault('pl_PL');

    $intlDate = new IntlDateFormatter(
        \Locale::getDefault(),
        IntlDateFormatter::FULL,
        IntlDateFormatter::FULL,
        $dateTime->getTimeZone(),
        IntlDateFormatter::GREGORIAN,
        'eeee, dd MMMM yyyy HH:mm:ss'
    );
}

printf(
    '%s<time datetime="%s">%s</time>%s',
    $tag,
    $dateTime->format($dateTime::ATOM),
    (is_null($intlDate)) ? $dateTime->format('Y-m-d H:i:s') : $intlDate->format($dateTime),
    str_replace('<', '</', $tag)
);
echo PHP_EOL;
