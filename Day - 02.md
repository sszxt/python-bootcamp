# 🐍 Python Basics – Part 2

## 1. Primitive Data Types

Primitive data types are the basic building blocks in Python:

|Type|Example|Description|
|---|---|---|
|`int`|`10`, `-5`|Whole numbers|
|`float`|`3.14`, `-0.5`|Numbers with decimal point|
|`str`|`'Hello'`|Sequence of characters (text)|
|`bool`|`True`, `False`|Boolean values (logic)|

```python
age = 21             # int
height = 5.9         # float
name = "Sam"         # str
is_coder = True      # bool
```

---

## 2. Type Error

Occurs when an operation is performed on incompatible data types.

```python
print("Age: " + 25)   # ❌ TypeError: can’t concat str and int
```

### ✅ Fix:

```python
print("Age: " + str(25))   # ✔️ Correct
```

---

## 3. Type Checking

To check the data type of a value, use `type()`.

```python
print(type(25))         # <class 'int'>
print(type("hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
```

---

## 4. Type Conversion (Casting)

Convert between data types using built-in functions:

```python
# str ➜ int
num = int("10")           # 10

# int ➜ str
text = str(10)            # '10'

# str ➜ float
pi = float("3.14")        # 3.14

# float ➜ int
value = int(3.99)         # 3 (truncated)
```

---

## 5. Math Operators

Python supports the following arithmetic operators:

|Operator|Description|Example|Result|
|---|---|---|---|
|`+`|Addition|`2 + 3`|`5`|
|`-`|Subtraction|`5 - 2`|`3`|
|`*`|Multiplication|`4 * 3`|`12`|
|`/`|Division (float)|`10 / 4`|`2.5`|
|`//`|Floor Division|`10 // 4`|`2`|
|`%`|Modulus (remainder)|`10 % 4`|`2`|
|`**`|Exponentiation|`2 ** 3`|`8`|

---

## 6. Number Manipulation

You can use functions for working with numbers:

```python
abs(-5)           # 5 (absolute value)
round(3.14159)    # 3
round(3.14159, 2) # 3.14

# Importing math module
import math
math.floor(3.9)   # 3
math.ceil(3.1)    # 4
math.sqrt(16)     # 4.0
```

---

## 7. F-Strings (Formatted Strings)

Used to embed expressions inside string literals. Introduced in Python 3.6+.

```python
name = "Sam"
age = 21

print(f"My name is {name} and I am {age} years old.")
# Output: My name is Sam and I am 21 years old.

# Expressions inside F-strings
print(f"Next year, I’ll be {age + 1}.")
```
