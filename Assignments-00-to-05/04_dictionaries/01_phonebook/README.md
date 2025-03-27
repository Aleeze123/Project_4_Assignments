# Phonebook Program📱

Welcome to the **Phonebook Program**! This Python program allows you to store and lookup phone numbers. The data is saved in a dictionary, and the program uses colorful output to enhance readability.

---

## 📋 Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [How to Use](#how-to-use)
4. [Contributing](#contributing)

---

## 🔥 Features
- **Store Contacts**: Add names and phone numbers to a phonebook.
- **Lookup Contacts**: Search for a phone number by entering a name.
- **Colorful Output**: Input prompts are displayed in **yellow**, results are printed in **cyan**, and errors are shown in **red** for easy identification.

---

## 🛠️ Installation

1. **Clone the Repository**:
    Clone the repository to your local machine using the following command:

    ```bash
    git clone https://github.com/Aleeze123/Project_4_Assignments
    ```

2. **Install Dependencies**:
    The program requires the `termcolor` library for colorful output. You can install it by running:

    ```bash
    pip install termcolor
    ```

    If you don't have `termcolor` installed, you will get an error. Ensure it's installed before running the program.

---

## 🚀 How to Use

1. **Run the Program**:
    Open your terminal or command prompt, navigate to the folder where the program is saved, and run the following command:

    ```bash
    python main.py
    ```

2. **Store Contacts**:
    The program will prompt you to enter a name and a phone number:

    ```plaintext
    Name:
    Number:
    ```

    Keep entering names and numbers. When you're finished, just hit **Enter** without typing any name (a blank line) to stop.

3. **Lookup Contacts**:
    After storing your contacts, you can look up phone numbers by entering a name:

    ```plaintext
    Enter name to lookup:
    ```

    If the name exists, it will display the phone number. If the name is not found, an error message will be displayed.

    Example:

    ```plaintext
    Enter name to lookup: Alice
    123-456-7890
    ```

    Or if the name is not found:

    ```plaintext
    Enter name to lookup: Bob
    Bob is not in the phonebook
    ```

---

## 🤝 Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Make changes on your fork.
3. Submit a pull request with your improvements.

---

Thank you for using the **Phonebook Program**! We hope it helps you stay organized. 📞
