# Random Module


To implement the randomness in the code, we can use the "random" module to generate random numbers

The random modules has lot of functions to perform random function on numbers.

before using the random module in code, we have to import the random package.

after that, we can use the random function like,
```
random.randint(a,b)
```

Return a random integer _N_ such that `a <= N <= b`. Alias for `randrange(a, b+1)`



##  1. What is the `random` Module?

The `random` module in Python is used to generate **pseudo-random numbers**.  
It can be used for:

- Random number generation
    
- Shuffling sequences
    
- Selecting random elements
    
- Simulating randomness in games, simulations, or testing
    

> **Note:** It does _not_ generate truly random numbers; it uses a deterministic algorithm called a pseudo-random number generator (PRNG).

---

## 2. What is a Module?

A **module** in Python is simply a **file containing Python code** (usually with a `.py` extension). It can define **functions**, **classes**, and **variables**, and include **executable code**.

### Why Use Modules?

- Code reuse
    
- Better organization
    
- Simplifies debugging
    
- Avoids code repetition
    

### How It Works

- You can **import** any module using `import` keyword.
    
- Python has many **built-in modules** like `math`, `random`, `os`, etc.
    

```python
import random
print(random.randint(1, 10))
```

### Creating Your Own Module

1. **Create a Python file** with your desired functions, e.g., `mymath.py`:
    

```python
# mymath.py
def add(a, b):
    return a + b
```

2. **Import and use it** in another file:
    

```python
import mymath
print(mymath.add(2, 3))  # Output: 5
```

---

## 3. Most Used and Famous `random` Module Functions

|Function|Description|Example|
|---|---|---|
|`random.random()`|Returns a float between `0.0` and `1.0`|`random.random()` → 0.8453|
|`random.randint(a, b)`|Returns a random **integer** between `a` and `b` (inclusive)|`random.randint(1, 6)`|
|`random.randrange(start, stop[, step])`|Returns a randomly selected element from `range(start, stop, step)`|`random.randrange(0, 100, 10)`|
|`random.choice(seq)`|Returns a random element from a non-empty sequence (list, tuple, etc.)|`random.choice(['a', 'b', 'c'])`|
|`random.choices(population, weights=None, k=1)`|Returns a list of `k` random elements (with replacement)|`random.choices([1, 2, 3], k=2)`|
|`random.sample(population, k)`|Returns `k` unique elements from the population (no replacement)|`random.sample([1, 2, 3, 4], 2)`|
|`random.shuffle(seq)`|Shuffles the sequence **in place**|`random.shuffle(my_list)`|

### **Lists in Python**

- A **list** is a collection that is ordered and mutable (can be changed).
    
- Lists can hold items of different data types (e.g., integers, strings, etc.).
    
- Defined using square brackets `[]`.
    

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
```

- Lists are **zero-indexed**, meaning the first element is at index `0`.
    

---

### **append()` Method**

- The `append()` method is used to **add a single item to the end of a list**.
    
- It modifies the original list in place.
    

**Syntax:**

```python
list_name.append(item)
```

**Example:**

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]
```

---

### **"Who Will Pay the Bill?" Game – Documentation Style**

This is a simple game where a random person from a list is chosen to pay the bill.

**Code Example (with documentation):**

```python
import random

def who_will_pay(names):
    """
    Selects one person at random from a list of names to pay the bill.

    Parameters:
    names (list): A list of names (strings).

    Returns:
    str: The name of the person who will pay the bill.
    """
    payer = random.choice(names)
    return f"{payer} is going to buy the meal today!"

# Example usage:
names = ["Alice", "Bob", "Charlie", "Diana"]
print(who_will_pay(names))
```

---

### **IndexError: list index out of range`**

- This error occurs when you try to **access an index that does not exist** in a list.
    

**Example:**

```python
fruits = ["apple", "banana"]
print(fruits[3])  # Error: IndexError: list index out of range
```

- **Why it happens:**  
    In the above case, the list only has indices `0` and `1`. Index `3` is invalid.
    
- **How to prevent it:**
    
    - Use `len()` to check the list size before accessing.
        
    - Ensure your loop or access logic stays within bounds.
        

**Safe access example:**

```python
index = 2
if index < len(fruits):
    print(fruits[index])
else:
    print("Index is out of range.")
```

---
