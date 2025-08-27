"""
NOTES DAY 1 — Syntax, Types, Operators, Conditionals
Goal: understand WHAT each thing is and HOW to use it with simple examples.
Run with:  python Week1/Monday/clear_notes.py
"""

print("=== 0) Comments, printing, and indentation ===")
# Comment: used to explain your code; Python ignores it when running.
# print() shows text or values on screen.
# "Indentation" (4 spaces) defines blocks: e.g., the body of an if.

print("Hello world")  # output: Hello world


print("\n=== 1) Variables and types ===")
# Variable: a name that points to a value stored in memory.
# Basic types:
#   int   -> integers (e.g., 3, -1, 0)
#   float -> decimals (e.g., 3.14, -0.5)
#   str   -> text (strings) "hello"
#   bool  -> boolean (True/False)

age = 21  # int
pi = 3.14159  # float
name = "Ada"  # str
active = True  # bool

print("Types:", type(age), type(pi), type(name), type(active))
# Example of use:
# - store data (age, price, name)
# - then operate with them
price = 5.0
quantity = 3
total = price * quantity
print("Total:", total)  # 15.0


print("\n=== 2) Type conversion (casting) ===")
# 'casting' = convert a value to another type when it makes sense.
# int("42") -> 42 ; float("3.5") -> 3.5 ; str(123) -> "123"
# Useful when reading user input (which comes as text) and needing it as a number.

text_num = "42"
n = int(text_num)
print("42 + 1 =", n + 1)  # 43


# Common error handling: converting text that is NOT a number.
def safe_to_float(s):
    try:
        return float(s)
    except ValueError:
        return None


print("safe_to_float('3.14') ->", safe_to_float("3.14"))  # 3.14
print("safe_to_float('abc')  ->", safe_to_float("abc"))  # None


print("\n=== 3) Arithmetic operators and precedence ===")
# Arithmetic: +, -, *, /, //, %, **
# /  -> real division
# // -> integer division (truncates)
# %  -> remainder (modulo)
# ** -> power
print("2 + 3 * 4 =", 2 + 3 * 4)  # 14 (multiplication before addition)
print("(2 + 3) * 4 =", (2 + 3) * 4)  # 20 (parentheses change order)
print("7 // 3 =", 7 // 3)  # 2
print("7 % 3  =", 7 % 3)  # 1
print("2 ** 5 =", 2**5)  # 32


print("\n=== 4) Comparison and logical operators ===")
# Comparison: ==, !=, >, >=, <, <=
# Return bool (True/False).
# Logical: and, or, not (combine conditions)
print("5 > 3  ->", 5 > 3)  # True
print("5 == 3 ->", 5 == 3)  # False
age = 18
has_id = True
can_enter = (age >= 18) and has_id
print("Can enter:", can_enter)  # True only if both are True
# or -> True if at least one condition is True
# not -> inverts True/False


print("\n=== 5) Input and output (input/print) ===")
# input() reads text from user and ALWAYS returns str.
# To use as number, convert it (int/float).
# (Uncomment to test interactively)
# data = input('Give me a number: ')
# try:
#     n = float(data)
#     print(f"The double is {n * 2}")  # f-string: convenient way to format text
# except ValueError:
#     print("⚠️ Please enter a valid number.")


print("\n=== 6) Strings (str) and f-strings ===")
# str: text; can be concatenated and formatted.
name = "Ada"
language = "Python"
print("Concatenation:", name + " loves " + language)
print(f"f-string: {name} loves {language}")  # more readable
# Useful methods:
print("python".upper())  # "PYTHON"
print("  hello  ".strip())  # "hello"
print("abc123".isalnum())  # True


print("\n=== 7) Conditionals if / elif / else ===")
# Structure to make decisions based on conditions.
score = 83
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D/F"
print("Grade:", grade)  # B


# Practical example: classify number as even/odd and its sign
def classify_number(n):
    tags = []
    tags.append("even" if n % 2 == 0 else "odd")
    if n > 0:
        tags.append("positive")
    elif n < 0:
        tags.append("negative")
    else:
        tags.append("zero")
    return ", ".join(tags)


print("6 ->", classify_number(6))  # even, positive
print("-5 ->", classify_number(-5))  # odd, negative
print("0 ->", classify_number(0))  # even, zero


print("\n=== 8) Common errors and how to avoid them ===")
# 1) Using = instead of == inside an if (in Python this is a SyntaxError).
#    if x = 5:  # ❌ incorrect
#    if x == 5: # ✅ correct
#
# 2) Forgetting to convert input to a number:
#    n = input("...")         # n is str
#    total = n + 1            # ❌ TypeError
#    total = int(n) + 1       # ✅
#
# 3) Wrong indentation (mixing spaces and tabs or misaligning blocks).
#    Use 4 spaces per block level.


print("\n=== 9) Mini guided practice ===")
# Goal: read temperature and convert C ↔ F
# - Didactic demo (no regex, step by step)
example = "20 C"
parts = example.split()  # ["20", "C"]
value = float(parts[0])
unit = parts[1].upper()
if unit == "C":
    conv = value * 9 / 5 + 32
    print(f"{value} C = {conv:.1f} F")  # 20.0 C = 68.0 F
elif unit == "F":
    conv = (value - 32) * 5 / 9
    print(f"{value} F = {conv:.1f} C")
else:
    print("Invalid unit (use C or F)")

print("\nEnd of notes. ✨ Practice by running Monday’s katas.")
