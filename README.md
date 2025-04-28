# Setting-up-authorization
This project implements a basic user authorization system in Python. It allows users to log in using a username and password, which are stored securely in an encrypted format.

## Features
*   **Password Encryption:** User passwords are encrypted using the Fernet symmetric encryption library, ensuring that they are not stored in plain text.
*   **Secure Storage:** Encrypted passwords, along with usernames, are stored in a `password.txt` file.
*   **User Authentication:** The system prompts users for their username and password and verifies them against the stored credentials.
*   **Error Handling:** Provides feedback to the user if the login attempt fails due to incorrect credentials.
## Prerequisites
*   **Python 3.x:** This project requires Python 3 or later.
*   **Cryptography Library:** You need to install the `cryptography` library. You can install it using pip:
    ```bash
    pip install cryptography
    ```
## How It Works
1.  **Key Generation (in `main.py`):**
    *   The `main.py` file (not provided, but inferred) is expected to generate a unique encryption key using `Fernet.generate_key()`.
    *   This key is then saved to a file named `key.key`.
    *   The `load_key()` function in `main.py` reads this key from the `key.key` file.
2.  **Password Encryption (in `main.py`):**
    *   When a new user is added, the password should be encrypted using the `Fernet` object and the loaded key.
    *   The encrypted password, along with the username, is stored in the `password.txt` file.
3.  **Authorization (in `authorization.py`):**
    *   The `authorization()` function takes the user's input username and password, along with the `Fernet` object.
    *   It reads each line from `password.txt`, splits it into username and encrypted password.
    *   It decrypts the stored password using the `Fernet` object.
    *   It compares the decrypted password with the user's input password.
    *   If both the username and password match, it returns `True`; otherwise, it continues to the next line.
    *   If no match is found after checking all lines, it returns `False`.
4.  **Main Loop (in `authorization.py`):**
    *   The `main()` function loads the encryption key and creates a `Fernet` object.
    *   It enters a loop that prompts the user for their username and password.
    *   It calls the `authorization()` function to verify the credentials.
    *   If the credentials are valid, it prints "Вы авторизованы" and exits the loop.
    *   If the credentials are not valid, it prints "Неверный логин или пароль. Попробуйте еще раз." and continues the loop.
## How to Run
1.  **Ensure you have `main.py` and `key.key`:** You need to create a `main.py` file that generates the key and saves it to `key.key`. You will also need to add users to the `password.txt` file.
2.  **Run `authorization.py`:**
    ```bash
    python authorization.py
    ```
3.  **Enter Credentials:** The program will prompt you to enter your username and password.
## Security Considerations
*   **Key Management:** The security of this system relies heavily on the secrecy of the encryption key. Ensure that the `key.key` file is stored securely and is not accessible to unauthorized users.
*   **Password Complexity:** While this system encrypts passwords, it does not enforce password complexity rules. It's recommended to add such rules in a real-world application.
*   **Salt:** For enhanced security, consider adding a salt to the password before encryption.
*   **File Permissions:** Set appropriate file permissions on `password.txt` and `key.key` to prevent unauthorized access.
* **main.py:** The `main.py` file is not provided, so it is assumed that it exists and is responsible for key generation and user creation.
## Future Improvements
*   **User Management:** Implement functions to add, delete, and modify user accounts.
*   **Password Complexity Enforcement:** Add rules to ensure users choose strong passwords.
*   **Salting:** Add salting to the password hashing process.
*   **Error Handling:** Implement more robust error handling for file operations and other potential issues.
*   **Logging:** Add logging to track login attempts and other events.
* **More secure key storage:** Consider using environment variables or a dedicated key management system.
* **Hashing:** Consider using a hashing algorithm like bcrypt instead of encryption for storing passwords.
