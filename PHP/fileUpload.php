<?php

if (isset($_FILES['file'])) {
    $file = $_FILES["file"];
    move_uploaded_file($file['tmp_name'], 'uploads/' . $file['name']);
    ech "File uploaded!";
}

?>

