# Python_Basics

01_print

02_numbers_and_math

03_variables

04_strings

05_input

06_type_conversion

07_conditions

08_loops

09_functions

10_basic_data_structures

______________________________________________________________________________________________________________________________________________________________________________________________________

Print Statement

The `print()` function is used to display output to the screen.

It is often the first instruction learned in any programming language.

Example:
```python
print("Hello, world!")

```
_______________________________________________________________________________________________________________________________________________________________________________________________________

numbers_and_math

```python
#This program adds two numbers

num1 = 1
num2 = 2

#Add two numbers

sum = num1 + num2

#Display the sum

print("The sum of the numbers is:", sum)
```


---

#Python supports basic arithmetic operations.

Examples:
```python
print(5 + 3)
print(10 - 4)
print(6 * 2)
print(8 / 2)
```







### Python_Introduction
Understanding Python: The Language of Instructions

Just as humans use language to communicate and exchange instructions, computers do the same. However, computers communicate using specialized languages such as Python, C++, and Java. To deliver instructions to a machine, programmers must organize their ideas and concepts into a language the computer can process.

### Syntax vs. Semantics

## Syntax:
This consists of the words representing objects and commands, along with punctuation that provides structure, hierarchy, and context to the code.

## Semantics:
This is the actual meaning conveyed by the syntax. While syntax is the "grammar," semantics is the "intent" behind the operations.

### How to Master the Language:

Exposure: The best way to learn is through consistent practice and reading code written by others.

Style Conventions: Professional developers follow general conventions (such as PEP 8) to maintain stylistic uniformity and readability within the language.

#

### Variables: 
These represent stored data as strings, sets, dictionaries, lists, and objects (Note: Future readings will explain these categories).



##




## the first command in python is 'print' this command for print and external the output

```python
print("Hello World") # Hello World


# the type of data is 4
# string / integer / float / boolean

print(type("Hello World")) #<class 'str'>
print(type(2)) #<class 'int'>
print(type(2.3)) #<class 'float'>
print(type(True)) # <class 'bool'>

# implicit conversion
print(7+3.14) # 10.14
print("a"+"b"+"c"+"d") #abcd
print("this " + "is " + "jamal's " + "car") # this is jamal's car

# Explicit conversion
base = 8
height = 2
area = (base * height)/2
print("The area of the tringle is:" +str( area)) # The area of the tringle is:8.0


```

```
important
1- variables
2- values
3- Expressions
4- Conversions

```







#  Python Core Basics
# Expressions, Variables, and Data Types

--------------------------------------------------
```python
1) Expressions

An expression is a combination of values, variables, and operators that Python evaluates to produce a result.

Examples:
    5 + 3
    x * 10
    "Hello " + "World"

--------------------------------------------------

2) Data Types

Data types define the kind of value stored in a variable and determine what operations can be performed on it.

Common data types:
    int     -> Integer
    float   -> Floating-point number
    str     -> String
    bool    -> Boolean (True / False)
    list    -> List
    tuple   -> Tuple (immutable)
    dict    -> Dictionary (key → value)
    set     -> Set (unique values)

--------------------------------------------------

3) Variables

A variable stores a value in memory and can change during program execution.

Examples:
    x = 10
    name = "Jamal"
    price = 12.5

--------------------------------------------------

4) Implicit Type Conversion

Implicit conversion occurs when Python automatically converts one data type to another to safely perform an operation.

Example:
    result = 5 + 2.5
    type(result) -> float

Rule:
    Python converts to the more precise type.

--------------------------------------------------

5) Explicit Type Conversion

Explicit conversion happens when the programmer manually converts a value using built-in functions.

Functions:
    str()    -> convert to string
    int()    -> convert to integer
    float()  -> convert to float

Examples:
    int("25") + 5
    str(100)

--------------------------------------------------

6) Type Annotations

Type annotations improve code readability and documentation.

Examples:
    name: str = "Hello"
    count: int = 10
    price: float = 1.25

Note:
    Python does NOT enforce types at runtime.

--------------------------------------------------

7) Arithmetic Expressions

Example:
    hotel_room = 100
    tax = hotel_room * 0.08
    total = hotel_room + tax
    guests = 4
    share_per_person = total / guests

Wrong:
    "Each person pays: " + share_per_person

Correct:
    "Each person pays: " + str(share_per_person)

--------------------------------------------------

8) Printing Multiple Variables

Using + :
    "Hello " + name

Using commas (recommended):
    print("Hello", name)

--------------------------------------------------

9) Fixing Type Errors

Wrong:
    "5 * 3 = " + (5 * 3)

Correct:
    "5 * 3 = " + str(5 * 3)

--------------------------------------------------

10) ZeroDivisionError

Wrong:
    result = 7 / 0

Safe approach:
    if denominator != 0:
        result = numerator / denominator
    else:
        result = numerator

--------------------------------------------------

Key Takeaways:

- Python uses implicit conversion when safe
- Use explicit conversion to avoid errors
- Do not mix strings and numbers without conversion
- Type hints improve readability, not enforcement
- Always validate input in automation scripts
```
--------------------------------------------------











