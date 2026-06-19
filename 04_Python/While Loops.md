```python
# 1 > 3 # false - no loop
# 1 < 3 # true - loop

#while 1 < 3: # True
    #print("hello")

x = 0

while x < 10:
    print("hello")
    x += 1
```

---
---
---

This code demonstrates a **while loop** in Python.

A **while loop** repeats code **as long as a condition is true**.

```python
x = 0

while x < 10:
    print("hello")
    x += 1
```


### Step by step

1. `x = 0`

   This creates a variable named `x` and gives it the value `0`.

2. `while x < 10:`

   This means:

   > “Keep running the loop while `x` is less than `10`.”

3. `print("hello")`

   Each time the loop runs, it prints:

```python
hello
```


4. `x += 1`

   This increases `x` by `1` each time the loop runs.

   It is the same as writing:

```python
x = x + 1
```


### What happens?

The value of `x` changes like this:

```python
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```


When `x` becomes `10`, the condition `x < 10` becomes false, so the loop stops.

### Output

The word `"hello"` is printed **10 times**.

```python
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
```


### Important idea

If you forget this line:

```python
x += 1
```


then `x` would stay `0` forever, and the loop would never stop. That is called an **infinite loop**.
