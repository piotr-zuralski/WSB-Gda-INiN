<?php

$dateTime = new DateTime();
$tag = '<em>';
if ($dateTime->getTimestamp() % 2) {
    $tag = '<strong>';
}

printf(
    '%s<time datetime="%s">%s</time>%s',
    $tag,
    $dateTime->format($dateTime::ATOM),
    $dateTime->format('Y-m-d H:i:s'),
    str_replace('<', '</', $tag)
);
