```python

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")

```

```python

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")

```

# Code Explanation: if-else vs if-elif-else

Both code blocks do the **same thing**, but they demonstrate two different ways to structure conditional statements in Python.

## First Version (Nested if-else)

```python
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")
```

**How it works:**
1. Checks if username is **less than 3 characters**
2. If true, prints the error message and stops
3. If false, enters the `else` block and checks **another condition** (nested if-else inside)
4. Checks if username is **more than 15 characters**
5. If true, prints the error message
6. If false, prints "Valid username"

**Problem:** The code is **indented deeply**, making it harder to read.

---

## Second Version (if-elif-else) ✅ Better

```python
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")
```

**How it works:**
- Same logic, but uses `elif` (else if) for clarity
- Checks conditions in order: first condition → second condition (`elif`) → default (`else`)
- **Cleaner and easier to read** with less indentation

---

## Key Differences

| Feature | Nested if-else | if-elif-else |
|---------|---|---|
| **Readability** | ❌ Hard to read (nested) | ✅ Easy to read (flat structure) |
| **Indentation** | Deep indentation | Shallow indentation |
| **Logic** | Same | Same |
| **Best for** | Simple cases | Multiple conditions |

---

## Example with Valid Username

```python
hint_username("alex")  # Output: "Valid username" (3-15 chars) ✅
hint_username("ab")    # Output: "Invalid username. Must be at least 3 characters long" ❌
hint_username("abcdefghijklmnopqrs")  # Output: "Invalid username. Must be at most 15 characters long" ❌
```

**Best Practice:** Use `if-elif-else` (second version) because it's cleaner and easier to maintain! 🎯
