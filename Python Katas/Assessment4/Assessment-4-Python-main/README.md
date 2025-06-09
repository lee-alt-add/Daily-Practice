# Python Practice Assessment: Core Skills

## Purpose
This assessment helps you practice foundational Python skills, focusing on data structures, functions, basic problem-solving, and understanding how unit tests verify your code. You will implement functions in `assessment.py`, and your solutions will be checked using `test_assessment.py`.

## Learning Outcomes Assessed
This assessment will test your:
- Understanding of **basic data structures** (like lists and dictionaries).
- Ability to write and use **functions** (defining them, using parameters, and returning values).
- **Problem-solving skills** by implementing simple algorithms.
- Ability to write code that passes pre-written **unit tests** and interpret test results to guide debugging.

## Files
- `assessment.py`: This is the file you need to edit. It contains function stubs that you must complete, according to their docstrings.
- `test_assessment.py`: This file contains unit tests. Run these tests to check if your functions in `assessment.py` work correctly. **Do not modify this file.** Your goal is to make all tests in this file pass.
- `README.md`: This file (you're reading it!).

## Instructions
1. **fork** this repository to your own GitHub account.
2. **Understand the Task:**
    *   Open `assessment.py`. For each function, carefully read its docstring. The docstring explains what the function should do, its parameters, and what it should return.

3. **Write Your Code:**
    *   Implement the logic for each function in `assessment.py`.

4. **Run the Unit Tests:**
    *   Open your terminal or command prompt.
    *   Navigate to the directory where you saved these files.
    *   Run the command:
        ```bash
        python -m unittest test_assessment.py
        ```

5.  **Interpret the Test Results:**
    *   If a test **FAILS**, the output will tell you:
        *   Which function failed.
        *   What input caused the failure.
        *   What output your function produced (`Actual`).
        *   What output the test expected (`Expected`).
    *   Use this information to find and fix the bugs in your `assessment.py` code.
    *   If all tests show **OK**, your implementations are correct, according to the tests!

6. **Iterate:**
    *   Modify your code in `assessment.py` based on the test feedback.
    *   Re-run the tests (`python -m unittest test_assessment.py`) until all tests pass.

Good luck with your assessment! This is a great opportunity to practice and improve your Python skills. If you have any questions, feel free to ask for help or clarification.