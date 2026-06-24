
```python
def area_triangle(base, height):
    return (base * height) / 2

area_a = area_triangle(5, 4)
area_b = area_triangle(10, 6)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))
```

this Python code calculates the areas of **two triangles**, adds them together, and prints the total.

```python
def area_triangle(base, height):
    return (base * height) / 2
```


This defines a function named `area_triangle`.

- `base` is the triangle’s base length
- `height` is the triangle’s height
- The area of a triangle is:

```plain text
(base × height) / 2
```


Then:

```python
area_a = area_triangle(5, 4)
```


This calculates the area of a triangle with:

- base = `5`
- height = `4`

So:

```plain text
(5 × 4) / 2 = 10
```


Next:

```python
area_b = area_triangle(10, 6)
```


This calculates another triangle’s area:

```plain text
(10 × 6) / 2 = 30
```


Then:

```python
sum = area_a + area_b
```


This adds both areas:

```plain text
10 + 30 = 40
```


Finally:

```python
print("The sum of both areas is: " + str(sum))
```


This prints:

```plain text
The sum of both areas is: 40.0
```


Small note: `sum` is also the name of a built-in Python function, so it’s usually better to use a name like `total_area` instead.
