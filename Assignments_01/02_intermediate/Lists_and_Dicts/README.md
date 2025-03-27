# Python List Practice and Index Game 🎮

## Problem #1: List Practice 🍎🍊🍇🍍

In this problem, you'll practice creating and manipulating lists in Python.

### Instructions:

1. Create a list called `fruit_list` that contains the following fruits:
   - 'apple', 'banana', 'orange', 'grape', 'pineapple'.
   
2. Print the length of the list.

3. Add 'mango' at the end of the list.

4. Print the updated list.

---

## Problem #2: Index Game 🎮

This problem helps you practice accessing and modifying elements in a list through a simple game.

### Instructions:

### 1. Initialize a List:
- Create a list with at least 5 different elements (numbers, strings, or a mix of both).

### 2. Accessing Elements:
- Write a function `access_element(lst, index)` that:
  - Accepts a list and an index as inputs.
  - Returns the element at the specified index.
  - If the index is out of range, return an appropriate message.

### 3. Modifying Elements:
- Write a function `modify_element(lst, index, new_value)` that:
  - Accepts a list, an index, and a new value as inputs.
  - Replaces the element at the specified index with the new value.
  - If the index is out of range, return an appropriate message.

### 4. Slicing the List:
- Write a function `slice_list(lst, start, end)` that:
  - Accepts a list, a start index, and an end index as inputs.
  - Returns a new list containing the elements from the start index up to (but not including) the end index.
  - Handles cases where the indices are out of range.

### 5. Game Interaction:
- Create a simple text-based game that:
  - Prompts the user to select an operation (access, modify, slice).
  - Asks for the necessary inputs (index, new value, etc.).
  - Displays the result and the updated list.

---

## Features ✨

- **List Creation & Manipulation**: Create and modify lists through simple operations.
- **Indexing & Slicing**: Practice accessing and slicing lists.
- **Text-based Game**: Engage with a fun game to practice list manipulation.
- **Error Handling**: Gracefully handle out-of-range index inputs with helpful messages.

---


## 🛠️ Installation

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