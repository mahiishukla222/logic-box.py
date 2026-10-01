# Pattern Generator and Number Analyzer

## 📌 Project Description

This is a simple Python program that provides a menu-driven system to:

1. Generate a star pattern
2. Analyze a range of numbers
3. Exit the program

The program uses `while` loop, `for` loop, `if-elif-else`, `range()`, user input, and the modulus `%` operator.

---

## 🛠️ Technologies Used

* Python 3
* `while` loop
* `for` loop
* `if-elif-else`
* `range()`
* `input()`
* Modulus operator `%`

---

## ⚙️ Features

### 1. Generate a Pattern

The user enters the number of rows, and the program generates a star pattern.

Example:

```text
*
**
***
****
*****
```

### 2. Analyze a Range of Numbers

The user enters a starting and ending number.

The program:

* Checks whether each number is **Even or Odd**
* Calculates the **sum of all numbers** in the given range

Example:

```text
Enter the start of the range: 1
Enter the end of range: 5

Number 1 is odd
Number 2 is even
Number 3 is odd
Number 4 is even
Number 5 is odd

Sum of all numbers from 1 to 5 is 15
```

### 3. Exit

The user can select option `3` to exit the program.

---

## 💻 Source Code

```python
print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        row = int(input("Enter the number of rows for the pattern: "))

        print("Pattern")
        for i in range(1, row + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0

        for num in range(start, end + 1):
            if num % 2 == 0:
                print("Number", num, "is even")
            else:
                print("Number", num, "is odd")

            total = total + num

        print("Sum of all numbers from", start, "to", end, "is", total)

    elif choice == 3:
        print("Exiting the program, Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
```

---

## 🧠 Concepts Learned

### `while True`

Used to keep the menu running until the user selects Exit.

### `for loop`

Used to generate the pattern and analyze numbers in a range.

### `if-elif-else`

Used to make decisions based on the user's choice and to check even/odd numbers.

### Modulus `%`

```python
num % 2 == 0
```

This checks whether a number is even.

### `range()`

```python
range(start, end + 1)
```

Used to generate numbers from the starting value to the ending value.

---

## ▶️ How to Run

1. Install Python 3.
2. Open IDLE, VS Code, PyCharm, or another Python editor.
3. Create a file named:

```text
pattern_analyzer.py
```

4. Paste the Python code into the file.
5. Run the program.
6. Select an option from the menu.

---
tructure

```text
Pattern-Generator-and-Number-Analyzer/
│
├── pattern_analyzer.py
└── README.md

Python Beginner Project
