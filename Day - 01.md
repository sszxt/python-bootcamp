
# 📘 Python Notes

## 1. Introduction to Python

Python is a high-level, interpreted programming language known for its readability and simplicity. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

### Key Features:

- Easy to learn and write
    
- Interpreted (no need for compilation)
    
- Dynamically typed
    
- Large standard library
    
- Portable and open-source
    

### Example:

```python
print("Hello, World!")
```

---

## 2. String Manipulation (Basics)

Strings in Python are sequences of characters enclosed in single `'` or double `"` quotes.

### String Declaration:

```python
text1 = "Hello"
text2 = 'World'
```

### Common Operations:

```python
# Concatenation
result = text1 + " " + text2  # Output: 'Hello World'

# Repetition
echo = text1 * 3              # Output: 'HelloHelloHello'

# Indexing
first_char = text1[0]        # Output: 'H'

# Slicing
partial = text1[1:4]         # Output: 'ell'

# Length
length = len(text1)          # Output: 5
```

---

## 3. Python `input()` Function

The `input()` function is used to take user input from the console as a **string**.

### Syntax:

```python
variable = input("Enter something: ")
```

### Example:

```python
name = input("Enter your name: ")
print("Hello, " + name)
```

> Note: Input is always received as a **string**. Use `int()` or `float()` for numeric input.

```python
age = int(input("Enter your age: "))
```

---

## 4. Python Variables

Variables are used to store data. Python is dynamically typed, meaning you don’t need to declare the type explicitly.

### Syntax:

```python
variable_name = value
```

### Example:

```python
name = "Alice"
age = 25
height = 5.7
is_student = True
```

---

## 5. Variable Naming Rules

To create valid and meaningful variable names:

### ✅ Valid Naming:

- Must start with a letter (a–z, A–Z) or an underscore `_`
    
- Can include letters, numbers, and underscores
    
- Case-sensitive (`Name` and `name` are different)
    

### ❌ Invalid Naming:

- Cannot start with a number (e.g., `1name`)
    
- Cannot use special characters (`@`, `-`, `#`, etc.)
    
- Cannot be a Python keyword (`class`, `for`, `if`, etc.)
    

### Good Practices:

- Use descriptive names: `user_age`, `total_price`
    
- Use lowercase letters with underscores for readability (snake_case)
    