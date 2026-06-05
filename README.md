#Python Calculator

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-1.0-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

![GitHub Stars](https://img.shields.io/github/stars/Adrish1100/Python_Calculator?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Adrish1100/Python_Calculator?style=social)
![GitHub Watchers](https://img.shields.io/github/watchers/Adrish1100/Python_Calculator?style=social)
![GitHub Issues](https://img.shields.io/github/issues/Adrish1100/Python_Calculator)
![Repo Views](https://komarev.com/ghpvc/?username=Adrish1100&repo=Python_Calculator&color=blue)

---

# 📌 Overview

A menu-driven Python calculator application that performs both basic arithmetic and mathematical operations using Python's built-in `math` module.

The calculator provides an interactive command-line interface (CLI) where users can repeatedly perform calculations without restarting the program.

This project is suitable for:

- Python beginners learning control structures
- Students practicing mathematical computations
- Understanding loops, conditionals, and pattern matching (`match-case`)
- Learning how to use Python's `math` library

---

# ✨ Features

## Basic Arithmetic Operations

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- Remainder Calculation (Modulo)

## Advanced Mathematical Operations

- Square Calculation
- Square Root Calculation
- Cube Calculation
- Cube Root Calculation
- Logarithm (Base 10)
- Logarithm (Base 2)
- Natural Logarithm (ln)

## User Interaction Features

- Menu-driven interface
- Continuous execution until user exits
- Input validation for operation selection
- Easy-to-use command-line navigation

---

# 🖥️ Sample Menu

```text
===========WELCOME TO MY CALCULATOR===========

1) DIVISION
2) MULTIPLICATION
3) ADDITION
4) SUBTRACTION
5) SQUARE
6) SQUARE ROOT
7) CUBE
8) CUBE ROOT
9) LOG BASE 10
10) LOG BASE 2
11) NATURAL LOG
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| math module | Mathematical calculations |
| match-case | Operation selection |
| while loops | Continuous execution |
| conditional statements | Input validation |

---

# 📚 Libraries Used

The project uses Python's built-in `math` module.

```python
from math import pow, sqrt, log, log2, log10, cbrt
```

### Imported Functions

| Function | Purpose |
|-----------|----------|
| `pow(x,y)` | Calculates powers |
| `sqrt(x)` | Square root |
| `cbrt(x)` | Cube root |
| `log(x)` | Natural logarithm |
| `log2(x)` | Base-2 logarithm |
| `log10(x)` | Base-10 logarithm |

---

# 🔍 Code Structure Analysis

## Variables

### `x`

Stores the first input number.

### `y`

Stores the second input number (for binary operations).

### `opt`

Stores the selected operation.

### `tryagain`

Controls valid menu selection.

### `maintry`

Controls whether the calculator should continue running.

---

## Control Flow

### Main Loop

```python
while(maintry == 1):
```

Keeps the calculator running until the user chooses to exit.

### Input Validation Loop

```python
while(tryagain == 1):
```

Ensures a valid operation is selected.

### Pattern Matching

```python
match opt:
```

Routes execution to the selected mathematical operation.

---

# 🚀 How To Run

## Clone Repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

## Navigate to Project

```bash
cd REPOSITORY
```

## Run Program

```bash
python calculator.py
```

---

# 📖 Supported Operations

| Option | Operation |
|----------|-----------|
| 1 | Division |
| 2 | Multiplication |
| 3 | Addition |
| 4 | Subtraction |
| 5 | Square |
| 6 | Square Root |
| 7 | Cube |
| 8 | Cube Root |
| 9 | Log Base 10 |
| 10 | Log Base 2 |
| 11 | Natural Log |

---

# 🔮 Possible Future Enhancements

The current project provides a strong foundation and can be expanded with additional features.

## Planned Improvements

### Scientific Calculator Features

- Trigonometric Functions
  - Sin
  - Cos
  - Tan
  - Cot
  - Sec
  - Cosec

### Advanced Mathematics

- Factorial
- Permutations & Combinations
- Exponential Functions
- nth Root Calculator
- Percentage Calculator

### Memory Operations

- Memory Store (MS)
- Memory Recall (MR)
- Memory Clear (MC)

### UI Improvements

- Colored terminal output
- Better menu design
- Error messages
- Progress indicators

### Error Handling

- Division by zero protection
- Invalid input handling
- Negative square root handling
- Logarithm domain validation

### Development Enhancements

- Object-Oriented Design
- Unit Testing
- GUI Version using Tkinter
- Web Version using Flask
- Package Distribution via PyPI

---

# ⚠️ Known Limitations

Current version has a few limitations:

- No exception handling for invalid numeric input.
- Division by zero can raise an error.
- Logarithm of non-positive values causes exceptions.
- Square root of negative numbers is not handled.
- Only integer inputs are accepted.
- No calculation history.

---

# 🏗️ Suggested Refactoring

Future code improvements could include:

- Function-based architecture
- Object-Oriented Programming (OOP)
- Separate modules for operations
- Better exception handling
- Cleaner menu management

Example:

```python
def addition(a, b):
    return a + b
```

This would improve readability and maintainability.

---

# 📊 Complexity Analysis

| Operation Type | Complexity |
|---------------|------------|
| Arithmetic Operations | O(1) |
| Logarithmic Operations | O(1) |
| Root Calculations | O(1) |
| Menu Processing | O(1) |

Overall Program Complexity:

```text
Time Complexity : O(1)
Space Complexity: O(1)
```

---

# 👨‍💻 Author

**Adrish Datta**

Python Developer | Software Enthusiast

---

# 🤝 Contributions

Contributions, issues, and feature requests are welcome.

Steps:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

---

# 📜 MIT License

MIT License

Copyright (c) 2026 Adrish Datta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
