
# 🐍 Python Notes: Control Flow and Conditionals

## 1. **Control Flow with `if`, `else`, and Conditional Operators**

Control flow lets us control which blocks of code run based on conditions.

### 🔹 Basic Syntax:

```python
if condition:
    # code block if condition is True
else:
    # code block if condition is False
```

### 🔹 Example:

```python
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### 🔹 Conditional Operators:

|Operator|Meaning|
|---|---|
|`==`|Equal to|
|`!=`|Not equal to|
|`>`|Greater than|
|`<`|Less than|
|`>=`|Greater than or equal|
|`<=`|Less than or equal|

---

## 2. **Intro to Modulo (`%`)**

The modulo operator returns the **remainder** after division.

### 🔹 Syntax:

```python
result = a % b
```

### 🔹 Example:

```python
print(10 % 3)  # Output: 1 (10 divided by 3 is 3 with remainder 1)
```

### 🔹 Use case:

Check if a number is even or odd:

```python
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 3. **Nested `if` Statements and `elif`**

### 🔹 Nested `if`: An `if` inside another `if`

```python
x = 10
if x > 0:
    if x < 20:
        print("x is between 1 and 19")
```

### 🔹 `elif` (short for else-if):

Used when you have multiple conditions.

```python
score = 75
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")
```

---

## 4. **Multiple `if` Statements**

Unlike `elif`, multiple `if` statements **can all run** if all conditions are true.

### 🔹 Example:

```python
x = 10
if x > 5:
    print("Greater than 5")
if x < 20:
    print("Less than 20")
# Both conditions are True, so both print
```

Use multiple `if` when **more than one condition** can be true **at the same time**.

---

## 5. **Logical Operators**

Used to combine multiple conditions.

|Operator|Description|Example|
|---|---|---|
|`and`|True if both are True|`a > 0 and a < 10`|
|`or`|True if at least one is True|`a < 0 or a > 100`|
|`not`|Reverses the condition|`not (a == 5)`|

### 🔹 Examples:

```python
x = 7
if x > 5 and x < 10:
    print("x is between 5 and 10")

if x < 5 or x > 10:
    print("x is outside the range")

if not x == 5:
    print("x is not 5")
```
