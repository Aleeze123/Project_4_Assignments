# 🎮 **Number Guessing Game** 🎲

Welcome to the **Number Guessing Game**! This Python program generates a random secret number between 1 and 99, and your goal is to guess it. The game gives helpful feedback (whether your guess is too low or too high) and ensures that you input a valid number.

The output is colorful, thanks to the `termcolor` library, to make the game more engaging and user-friendly. 🎨✨

---

## 📋 **Table of Contents**
1. [Features](#features) 🎉
2. [Installation](#installation) ⚙️
3. [How to Play](#how-to-play) 🎮
4. [Contributing](#contributing) 🤝

---

## 🔥 **Features**
- **🎯 Random Number**: The game generates a random number between 1 and 99.
- **🧩 Feedback**: You get real-time feedback on whether your guess is too low or too high.
- **💡 Input Validation**: The game ensures that the user enters a valid number, providing an error message if an invalid input is provided.
- **🌈 Colorful Output**: The game features colorful prompts, messages, and error alerts using the `termcolor` library.
- **🏆 Victory Message**: Once you guess correctly, you’ll receive a congratulatory message in green.

---

## 🛠️ **Installation**

1. **Clone the Repository**:
    Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/Aleeze123/Project_4_Assignments
    ```

2. **Install Dependencies**:
    The program requires the `termcolor` library for colorful output. You can install it by running:

    ```bash
    pip install termcolor
    ```

    Make sure to install this package before running the game.

---

## 🚀 **How to Play**

1. **Run the Game**:
    Open your terminal or command prompt, navigate to the folder where the program is saved, and run the following command:

    ```bash
    python main.py
    ```

2. **Guess the Number**:
    The game will prompt you to enter a guess:

    ```plaintext
    Enter a guess:
    ```

    You will receive feedback indicating whether your guess is too high or too low. The game will continue until you guess the correct number.

3. **Winning**:
    Once you guess the correct number, the game will congratulate you with a message like:

    ```plaintext
    Congrats! The number was: 42
    ```

4. **Error Handling**:
    If you enter an invalid input (like a letter or special character), the game will notify you to enter a valid number.

    ```plaintext
    Invalid input! Please enter a valid number.
    ```

---

## 🤝 **Contributing**

We welcome contributions to this project! If you'd like to improve the game or add new features, feel free to follow these steps:

1. **Fork the Repository**: Click on the **Fork** button at the top of the repository page.
2. **Make Changes**: Create a new branch, make your changes, and commit them.
3. **Submit a Pull Request**: Once you're happy with your changes, submit a pull request to the main repository.

---

🎉 Thank you for using the **Number Guessing Game**! Have fun and good luck guessing the number! 🎯
