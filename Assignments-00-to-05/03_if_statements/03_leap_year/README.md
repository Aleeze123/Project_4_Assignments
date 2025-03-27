# 📝 Leap Year Checker Program

Welcome to the **Leap Year Checker Program**! This Python program allows users to check whether a given year is a leap year or not, using the rules of the Gregorian calendar. The program utilizes the `termcolor` library to display colored output for better visual appeal.

---

## 📋 Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [How to Use](#how-to-use)
4. [Contributing](#contributing)

---

## 🔥 Features

- **Colorful Output**: 
  - The greeting message is displayed in **cyan**.
  - The input prompt is displayed in **yellow**.
  - Leap year results are shown in **green** if the year is a leap year, and **red** if it is not.
  
- **Leap Year Calculation**: 
  The program checks if the input year is a leap year by applying the following criteria:
  1. The year must be divisible by 4.
  2. If divisible by 100, the year must also be divisible by 400 to be a leap year.
  
- **Simple Interface**: The user simply needs to input a year, and the program will immediately tell them whether it's a leap year or not.

---

## 🛠️ Installation

To run the program, follow these steps:

1. **Clone the Repository**:
    Clone the repository to your local machine using the following command:

    ```bash
    git clone https://github.com/Aleeza123/Project_4_Assignments.git
    ```

2. **Install Dependencies**:
    This program uses the `termcolor` library for colorful output. Install it by running the following command:

    ```bash
    pip install termcolor
    ```

    The `termcolor` library is not part of Python's standard library, so make sure it's installed before running the program.

---

## 🚀 How to Use

1. **Run the Program**:
    Open your terminal or command prompt, navigate to the folder where the program is saved, and run the following command:

    ```bash
    python main.py
    ```

2. **Input the Year**:
    The program will prompt you to enter a year. Type the year you want to check and press **Enter**.

    Example input/output:
    ```plaintext
    Please input a year: 2024
    That's a leap year!  (Printed in green)
    ```

    If you input a non-leap year:
    ```plaintext
    Please input a year: 2023
    That's not a leap year.  (Printed in red)
    ```

---

## 🤝 Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Make changes on your fork.
3. Submit a pull request with your improvements.

---

Thank you for using the **Leap Year Checker Program**! We hope it helps you check leap years easily and in style! 🎉

---
