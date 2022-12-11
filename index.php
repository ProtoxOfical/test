<?php
function generateString() {
  // Generate a random string
  $randomString = bin2hex(random_bytes(16));

  // Return the string
  return $randomString;
}

// Set the content type to plain text
header("Content-Type: text/plain");

// Call the generateString function every 5 seconds
setInterval(generateString, 5000);
