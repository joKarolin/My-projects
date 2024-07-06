Welcome to the Security Tools Repository! This repository contains three distinct security-related projects: a Password Generator Tool, a Text Encryption Tool, and a Keylogger. Each project is implemented using Python and includes a web interface for user interaction, except for the Keylogger, which operates in the background.

Description
The Password Generator Tool generates secure, random passwords based on user-defined criteria such as length and character types (e.g., letters, numbers, special characters). The tool also includes a password strength indicator to help users create strong passwords.

Features
Generate passwords of customizable length.
Include or exclude letters, numbers, and special characters.
Password strength indicator.

Technology
Backend: Python 3
Frontend: HTML
Integration: Flask


Text Encryption Tool
Description
The Text Encryption Tool allows users to encrypt and decrypt text using a combination of Caesar cipher and Vigenere cipher. This tool provides an extra layer of security by combining two encryption methods.

Features
Encrypt and decrypt text using Caesar cipher and Vigenere cipher.
Handle case sensitivity in the encryption and decryption processes.
User-friendly interface.

Technology
Backend: Python 3
Frontend: HTML
Integration: Flask


Keylogger
Description
The Keylogger is a background tool that records keystrokes on a device and stores them in a text file. It is designed to run invisibly without a user interface.

Features
Record all keystrokes on the device.
Store keystrokes in a text file.
Operate invisibly in the background.

Technology
Backend: Python 3


To run these tools locally, follow these steps:
Clone the repository.
Set up a virtual environment and install dependencies.
Run the Flask applications.
For the Password Generator Tool and Text Encryption Tool, navigate to their respective directories and run them.
The Keylogger can be run directly as a Python script.

Password Generator Tool
Open your web browser and navigate to http://localhost:5000.
Adjust the settings for password length and character types.
Click "Generate" to create a new password.
Check the password strength indicator for guidance.

Text Encryption Tool
Open your web browser and navigate to http://localhost:5000.
Enter the text you want to encrypt or decrypt.
Select the encryption or decryption method (Caesar or Vigenere cipher).
Click "Encrypt" or "Decrypt" to process the text.

Keylogger
Run the keylogger.py script.
The keylogger will start recording keystrokes in the background.
To view the recorded keystrokes, open the generated log file.
