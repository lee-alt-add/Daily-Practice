
<?php

if (isset($_POST['name'])) {
    echo "Hello, " . htmlspecialchars($_POST["name"]) . "!";
}

?>

<form method="POST">
    <input type="text" name="name" placeholder="Enter name">
    <button type="submit">Greet</button>
</form>