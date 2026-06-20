```python

################
#comparison operators

# ==
# !=
# >
# <
# >=
# <=

##################

print(10 == 10) # True
print(10 != 10) # False

if 10 == 10:
    print("these numbers are identical ")
else:
    print("these numbers are not identical")


name = input("what is your name?")
if name == "jamal":
    print("take the ball jamal")

else:
    print("no ball for you")
```




---
---
## Comparison operators in Python

Comparison operators are used to **compare two values**.  
The result is always a **Boolean value**:

```python
True
False
```


## Common comparison operators

```python
==   # equal to
!=   # not equal to
>    # greater than
<    # less than
>=   # greater than or equal to
<=   # less than or equal to
```


## Examples

```python
print(10 == 10)
```


This means:

> Is `10` equal to `10`?

The answer is:

```python
True
```


Another example:

```python
print(10 != 10)
```


This means:

> Is `10` **not equal** to `10`?

The answer is:

```python
False
```


Because `10` and `10` are the same.

## Using comparisons with `if`

Comparison operators are often used inside `if` statements:

```python
if 10 == 10:
    print("these numbers are identical")
else:
    print("these numbers are not identical")
```


Since `10 == 10` is `True`, Python runs the first block:

```python
these numbers are identical
```


## Comparing text

You can also compare strings:

```python
name = input("what is your name?")

if name == "jamal":
    print("take the ball jamal")
else:
    print("no ball for you")
```


This checks whether the user typed exactly:

```python
jamal
```


If they did, the first message prints.  
If they typed anything else, the `else` message prints.

## Important note

String comparison is **case-sensitive**.

So these are different:

```python
"jamal"
"Jamal"
"JAMAL"
```


If you want to ignore uppercase/lowercase differences, you can use:

```python
name = input("what is your name?").lower()

if name == "jamal":
    print("take the ball jamal")
else:
    print("no ball for you")
```


Here, `.lower()` changes the user’s input to lowercase before comparing it.


