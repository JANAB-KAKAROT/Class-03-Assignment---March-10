# Lesson 05: Control Flow & Loops
# Example 1: Conditional Statements
# Checking a number's nature with a conversational approach
try:
    num = int(input("Hmm, what's the number you're thinking of? "))
    if num > 0:
        print("Ah, that's a positive one!")
    elif num < 0:
        print("Oh, a negative number. Tough luck!")
    else:
        print("Zero! The perfect balance.")
except ValueError:
    print("That's not a valid number, my friend.")

# Example 2: Nested if Statements
try:
    num = int(input("Give me a number, let's see if it's even or odd: "))
    if num >= 0:
        print("It's even.") if num % 2 == 0 else print("That's an odd one.")
    else:
        print("Negative numbers? Hmm, let's not go there.")
except ValueError:
    print("Oops! That's not a valid number.")

# Example 3: Simple Calculator (with a twist)
operation = input("Pick an operation (+, -, *, /): ")
try:
    num1 = float(input("First number, please: "))
    num2 = float(input("And the second number: "))

    if operation == '+':
        print("Adding them up gives: ", num1 + num2)
    elif operation == '-':
        print("Subtracting them results in: ", num1 - num2)
    elif operation == '*':
        print("Multiplication magic: ", num1 * num2)
    elif operation == '/':
        print("Divide and conquer: ", num1 / num2) if num2 != 0 else print("Division by zero? Not today.")
    else:
        print("That's an unusual operation.")
except ValueError:
    print("Hmm, that doesn't seem right.")

# Example 4: Grading System (keeping it casual)
try:
    marks = float(input("Enter your marks (0-100): "))
    grade = "A+" if marks >= 90 else "A" if marks >= 80 else "B" if marks >= 70 else "C" if marks >= 60 else "D" if marks >= 50 else "F"
    print(f"You scored a {grade}. Keep it up!")
except ValueError:
    print("Those don't look like marks to me.")
