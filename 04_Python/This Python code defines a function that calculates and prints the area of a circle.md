```python 

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)
circle_area(10)
circle_area(15)

```

---
---

This Python code defines a function that calculates and prints the area of a circle.

```python
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)
```


### What it does

- `def circle_area(radius):`  
  Defines a function named `circle_area`.  
  It takes one input value: `radius`.

- `pi = 3.14`  
  Stores an approximate value of π.

- `area = pi * (radius ** 2)`  
  Calculates the circle’s area using the formula:

```plain text
area = π × radius²
```


- `print(area)`  
  Displays the calculated area.

Then the function is called three times:

```python
circle_area(5)
circle_area(10)
circle_area(15)
```


So it calculates areas for circles with radii `5`, `10`, and `15`.

### Output

```plain text
78.5
314.0
706.5
```
