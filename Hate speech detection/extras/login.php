<?php
include 'config.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT password FROM users WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    $stmt->bind_result($hashedPassword);

    if ($stmt->fetch() && password_verify($password, $hashedPassword)) {
        echo json_encode(['message' => 'Login successful!']);
    } else {
        echo json_encode(['message' => 'Invalid username or password!']);
    }

    $stmt->close();
    $conn->close();
}
?>
