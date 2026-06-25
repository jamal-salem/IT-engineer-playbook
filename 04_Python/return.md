```python


def is_even(number):
    if number % 2 == 0:
        return True   # إذا كان زوجياً، يرجع True ويخرج فوراً من الدالة
    return False      # لن يصل الكمبيوتر هنا إلا إذا كان الرقم فردياً

```

---
---
----

# Return Statement in Python

The code demonstrates how the `return` statement works in Python. Here's what's happening:

## Function Breakdown

```python
def is_even(number):
    if number % 2 == 0:
        return True   # إذا كان زوجياً، يرجع True ويخرج فوراً من الدالة
    return False      # لن يصل الكمبيوتر هنا إلا إذا كان الرقم فردياً
```

**What it does:**
- **Checks if a number is even** using the modulo operator (`%`)
- `number % 2 == 0` means: if the remainder when dividing by 2 equals 0, the number is even

## Key Points About `return`

1. **Exits the function immediately**: When `return` is executed, the function stops and sends a value back to the caller
2. **First condition matched**: If the number is even, it returns `True` right away and never reaches the second `return`
3. **Default case**: If the number is odd (the first condition is false), it returns `False`

## Example Usage

```python
is_even(4)   # Returns True (4 % 2 == 0)
is_even(7)   # Returns False (7 % 2 == 1, not 0)
```

## Why This Matters

The `return` statement is crucial because:
- It **stops function execution** — any code after `return` won't run
- It **sends data back** — the calling code receives the returned value
- It makes code **more efficient** — no need to check unnecessary conditions once you have your answer

This is a clean, simple example of using `return` to exit a function early when a condition is met.
