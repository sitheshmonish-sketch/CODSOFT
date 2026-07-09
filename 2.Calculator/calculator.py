# **Project Title: Calculator Using Python**

## **Project Description**

A **Calculator** is a basic Python project that performs simple arithmetic operations. The application prompts the user to enter two numbers and choose an arithmetic operation such as addition, subtraction, multiplication, or division. Based on the user's choice, the program performs the calculation and displays the result.

This project helps beginners understand Python fundamentals, including user input, conditional statements, functions, and arithmetic operators.

---

## **Objectives**

* Perform basic arithmetic operations.
* Accept user input for numbers and operation selection.
* Display accurate calculation results.
* Handle invalid inputs gracefully.

---

## **Features**

* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Input validation
* Division-by-zero error handling
* Simple menu-driven interface

---

## **Tools and Technologies**

* **Programming Language:** Python 3
* **IDE:** VS Code / PyCharm / IDLE

---

## **Python Code**

```python
# Simple Calculator

print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    print("Result =", num1 + num2)

elif choice == "2":
    print("Result =", num1 - num2)

elif choice == "3":
    print("Result =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid choice!")
```

---

## **Sample Output**

### Addition

```text
===== SIMPLE CALCULATOR =====

Enter first number: 10
Enter second number: 5

Choose Operation
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

Enter your choice (1/2/3/4): 1

Result = 15.0
```

### Division

```text
===== SIMPLE CALCULATOR =====

Enter first number: 20
Enter second number: 4

Choose Operation
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

Enter your choice (1/2/3/4): 4

Result = 5.0
```

---

## **Workflow**

1. Start the program.
2. Enter the first number.
3. Enter the second number.
4. Select an arithmetic operation.
5. Perform the calculation.
6. Display the result.
7. Exit the program.

---

## **Advantages**

* Simple and easy to use.
* Performs calculations quickly.
* Helps beginners understand Python basics.
* Demonstrates conditional statements and user input.

---

## **Applications**

* Basic mathematical calculations.
* Educational purposes.
* Learning Python programming concepts.
* Small utility program for everyday use.

---

## **Future Enhancements**

* Scientific calculator functions (square root, power, logarithms).
* Graphical User Interface (GUI) using Tkinter.
* History of calculations.
* Percentage and modulus operations.
* Keyboard-based operation selection.

---

## **Learning Outcomes**

By completing this project, you will learn:

* Python input and output
* Arithmetic operators
* Conditional statements (`if`, `elif`, `else`)
* Error handling
* Menu-driven program development

---

## **Conclusion**

The **Calculator Using Python** project is a beginner-friendly application that demonstrates the use of arithmetic operators, conditional statements, and user input. It provides a practical understanding of Python programming and serves as a foundation for developing more advanced calculator applications with additional mathematical functions and graphical interfaces.
