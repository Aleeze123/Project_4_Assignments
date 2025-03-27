# 🔐 Powerful Password Program 🔑

Welcome to the **Powerful Password Program**! This Python program uses password hashing to securely verify user logins. Instead of storing actual passwords, it stores hashed versions of passwords and compares them when you try to log in. The program uses the SHA256 hash function to ensure password security, and it provides colorful output with the help of the `termcolor` library to make your login experience more engaging. 🌟

---

## 📋 Table of Contents
1. [Features](#features) ✨
2. [Installation](#installation) ⚙️
3. [How to Use](#how-to-use) 🚀
4. [Contributing](#contributing) 🤝

---

## 🔥 Features
- **🔒 Password Hashing**: The program uses the SHA256 hashing algorithm to store passwords securely.
- **📧 Login Validation**: It checks whether the hashed password entered matches the stored hash for a specific email.
- **🌈 Colorful Output**: The program uses the `termcolor` library to highlight login results in different colors (e.g., green for success, red for failure).
- **🔑 Secure User Authentication**: Provides a secure way of checking credentials without storing plain-text passwords.

---

## 🛠️ Installation

1. **Clone the Repository**:
    Clone the repository to your local machine using the following command:

    ```bash
    git clone https://github.com/Aleeze123/Project_4_Assignments
    ```

2. **Install Dependencies**:
    The program requires the `termcolor` library for colorful output. You can install it using the following command:

    ```bash
    pip install termcolor
    ```

    If you don't have `termcolor` installed, you'll get an error. Please make sure to install it before running the program.

---

## 🚀 How to Use

1. **Run the Program**:
    Open your terminal or command prompt, navigate to the folder where the program is saved, and run the following command:

    ```bash
    python main.py
    ```

2. **Login Attempts**:
    The program will check several login attempts and display whether each one is successful or not. Here's an example of what the output might look like:

    ```plaintext
    Login attempt for example@gmail.com with password 'word': False (in red)
    Login attempt for example@gmail.com with password 'password': True (in cyan)
    Login attempt for code_in_placer@cip.org with password 'Karel': False (in red)
    Login attempt for code_in_placer@cip.org with password 'karel': True (in cyan)
    Login attempt for student@stanford.edu with password 'password': False (in red)
    Login attempt for student@stanford.edu with password '123!456?789': False (in red)
    ```

3. **View Results**:
    After entering the email and password, the program will display the result:
    - **Red**: Failed login attempt.
    - **Cyan**: Successful login attempt.

---

## 🤝 Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. **Fork the repository**: Click the "Fork" button on the top right of the repository page to create a copy under your GitHub account.
2. **Make changes on your fork**: Clone your fork and make any changes or additions.
3. **Submit a pull request**: Once you're satisfied with your changes, submit a pull request (PR) to the main repository with a description of what you've changed.

---

🎉 Thank you for using the **Powerful Password Program**! We hope it keeps your online credentials safe and sound. Stay secure and happy coding! 🔑💻
