```python

name = "Jamal"
number = len(name) * 9
print("Hello " + name + ".your lucky number is " + str(number) + "")

name = "salem"
number = len(name) * 9
print("Hello " + name + ".your lucky number is " + str(number) + "")

```

this Python code calculates a **“lucky number”** based on the length of a name.

```python
name = "Jamal"
number = len(name) * 9
print("Hello " + name + ".your lucky number is " + str(number) + "")
```


### What each line does

- `name = "Jamal"`  
  Stores the text `"Jamal"` in a variable called `name`.

- `len(name)`  
  Counts how many characters are in the name.  
  `"Jamal"` has **5** letters.

- `number = len(name) * 9`  
  Multiplies the length of the name by `9`.  
  So: `5 * 9 = 45`.

- `print(...)`  
  Displays the message on the screen.

Because `number` is an integer, `str(number)` converts it into text so it can be joined with the other strings.

The second part does the same thing for `"salem"`:

```python
name = "salem"
number = len(name) * 9
print("Hello " + name + ".your lucky number is " + str(number) + "")
```


`"salem"` also has **5** letters, so the lucky number is also **45**.

### Output

```plain text
Hello Jamal.your lucky number is 45
Hello salem.your lucky number is 45
```


A slightly cleaner version would be:

```python
name = "Jamal"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))
```


Notice the space after the period: `. Your`  
That makes the sentence easier to read.
