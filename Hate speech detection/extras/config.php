<?php
$servername = "127.0.0.1";
$username = "root"; // your database username
$password = "srishti@2003"; // your database password
$dbname = "auth_demo";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
