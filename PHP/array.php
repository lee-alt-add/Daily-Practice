<?php

// Normal List
$names = ["John", "Jane", "Doe"];

// accessing List
print_r($names[0]); // 'John'

// remove
array_pop($names); // Removes the last element
print_r($names); 
// check existence
print_r(in_array("Jane", $names)); // 1
// combine lists
$others = ["Steve", "Peter", "Mary"];
print_r(array_merge($names, $others));
// sort
$numbers = [4, 2, 8, 1];

usort($numbers, function($a, $b) {
    return $a <=> $b;
});
print_r($numbers);

?>