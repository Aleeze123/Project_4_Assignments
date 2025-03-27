# Age Verification Program 👩‍⚖️

This Python program checks if a person is an adult based on their age. It uses a predefined age (18 years old) to classify someone as an adult. The program handles invalid inputs by prompting the user to enter a valid number if the input is incorrect. The program also uses the `termcolor` library to colorize the text output for better readability and aesthetics.

## Program Features ✨

- **Age Verification**: The program checks if the input age is greater than or equal to 18 (considered the legal adult age in the United States).
- **Error Handling**: The program ensures that the user inputs a valid integer. If the input is invalid (e.g., a string or symbol), the program will catch the error and ask the user to enter a valid integer.
- **Colorized Output**: The program uses the `termcolor` library to colorize:
  - The input prompt in **yellow**.
  - The result (`True` or `False`) in **cyan**.
  - Error messages in **red**.

## Dependencies 📦

- `termcolor`: A library for coloring text output in the terminal. 🌈


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