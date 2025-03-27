# Word-based Sentence Generator 📝

This Python program generates a sentence based on the part of speech of a word provided by the user. The program allows the user to input a word and choose whether it is a noun, verb, or adjective, then prints a sentence using that word in the appropriate template. The output is colorized using the `termcolor` library for improved readability and visual appeal.

## Program Features ✨

- **Dynamic Sentences**: Based on the user input, the program generates one of three sentence templates.
  - **Noun**: "I am excited to add this [word] to my vast collection of them!"
  - **Verb**: "It's so nice outside today it makes me want to [word]!"
  - **Adjective**: "Looking out my window, the sky is big and [word]!"
- **Colorful Output**: The output is colorized using the `termcolor` library, making it easier to distinguish different types of messages (e.g., sentences and error messages).
- **Error Handling**: If the user enters an invalid part of speech (not 0, 1, or 2), the program will print an error message in red.

## Dependencies 📦

- `termcolor`: A library used to colorize the terminal output for better readability and aesthetics. 🌈

## 🛠️ Installation

1. **Clone the Repository**:
    Clone the repository to your local machine using the following command:

    ```bash
    git clone https://github.com/Aleeze123/Project_4_Assignments
    ```

2. **Install Dependencies**:
    This program requires the `termcolor` library for colorful output. You can install it by running the following command:

    ```bash
    pip install termcolor
    ```

---