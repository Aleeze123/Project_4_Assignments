# 🧩 **Sudoku Solver** 🧠

Welcome to the **Sudoku Solver** project built with Python! This project uses the **backtracking algorithm** to solve any valid Sudoku puzzle. 🏆 The solution is achieved recursively by exploring every possible number placement until the puzzle is solved. The output is visually enhanced using the **termcolor** library, giving you a colorful experience. 🌈

---

## 🔑 **Features** ✨

- **Backtracking Algorithm**: Solves the Sudoku puzzle by trying different numbers for each empty cell until the correct solution is found. 🔄
- **Colorful Output**: Thanks to the `termcolor` library, the board is printed with colors, making it more engaging and easier to read. 🎨
  - **Blue** for numbers filled in the puzzle 💙
  - **Yellow** for empty cells (0) 💛
  - **Green** for the solved board 🟢
  - **Red** for error messages ❌
  - **Cyan** for headers and instructions 🟦
- **Works for any valid Sudoku puzzle**: Whether your puzzle is partially filled or completely empty, this solver can handle it! 🧩

---


### 🛠️ Installation

To run this program, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Aleeze123/Project_4_Assignments
    ```

2. **Install Dependencies**:
    The program uses the `termcolor` library for colorful terminal output. Install it by running:
    ```bash
    pip install termcolor
    ```

3. **Run the Program**:
    Once the dependencies are installed, run the program:
    ```bash
    python main.py
    ```

---