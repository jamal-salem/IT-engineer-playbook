```python
cars = ["audi\n", "toyota\n", "bmw\n"]
adjectives = ["(fast)" , "(expensive)\n"]

for car in cars:
    print(car + " | ")
    for adjective in adjectives:
        print(" - " + adjective)
```

# Here is an explanation of the code 

### Explanation

This code uses **nested `for` loops**.

A **nested loop** means there is one loop inside another loop.

---

### 1. The `cars` list

```python
cars = ["audi\n", "toyota\n", "bmw\n"]
```


This list contains three car names:

- `audi`
- `toyota`
- `bmw`

The `\n` means **new line**.  
So after printing each car name, Python moves to the next line.

---

### 2. The `adjectives` list

```python
adjectives = ["(fast)" , "(expensive)\n"]
```


This list contains two descriptions:

- `(fast)`
- `(expensive)`

---

### 3. The outer loop

```python
for car in cars:
    print(car + " | ")
```


This loop goes through each car in the `cars` list.

For each car, it prints the car name followed by `" | "`.

---

### 4. The inner loop

```python
for adjective in adjectives:
    print(" - " + adjective)
```


This loop runs **inside** the car loop.

For every car, Python prints all adjectives:

- `- (fast)`
- `- (expensive)`

---

### What happens step by step?

Python does this:

1. Takes `"audi\n"`
2. Prints it
3. Prints all adjectives
4. Takes `"toyota\n"`
5. Prints it
6. Prints all adjectives
7. Takes `"bmw\n"`
8. Prints it
9. Prints all adjectives

---

### Example output

The output will look similar to this:

```plain text
audi
 | 
 - (fast)
 - (expensive)

toyota
 | 
 - (fast)
 - (expensive)

bmw
 | 
 - (fast)
 - (expensive)
```


### Main idea

The code prints each car, and under each car it prints its adjectives.

So the idea is:

```plain text
For every car, print every adjective.
```
