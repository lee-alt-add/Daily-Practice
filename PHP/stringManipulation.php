<?php

$str = "Jane";

// Make uppercase
echo strtoupper($str);

// Make lowercase
echo strtolower($str);

// Get substring
echo substr($str, 0, 4);

// Remove whitespaces
echo trim($str);

// Get string length
echo strlen($str);

// Make string a list
echo explode(",", $str);

// Replace substring
echo str_replace("Jane", "John", $str);

// Check if string contains word
echo strpos($str, "Jane") !== false ? "Yes" : "No";

?>