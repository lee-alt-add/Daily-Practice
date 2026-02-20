<?php

function greet(string $name): string {
    return "Hello " . $name;
}

function add(int $a, int $b): int {
    return $a + $b;
}

function is_palindrome(string $string): bool {
    $result = "";

    for ($i = strlen($string) - 1; $i >= 0; $i--) {
        $result .= strtolower($string[$i]);
    }

    return $result === strtolower($string);
}

function reverse_words(string $str): string {
    $array = explode(" ", $str);
    $array = array_reverse($array);
    return implode(" ", $array);
}


?>