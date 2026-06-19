```python
age = input("Enter your age?\n ")
age = int(age)

if age > 17:
    print("you are elgibe to take a driver test")

else:
    print("you are not eligible to take a driver test")
    exit()

driver_test = input("Do you passed the driver test?\n ")

if driver_test == "yes":
    print("congratulations you are eligible to drive")

elif driver_test == "no":
    print("Sorry , you need to pass the driver test")

else:
    print("you need to enter yes or no")
```



This Python program checks whether a person is allowed to drive based on **age** and whether they **passed the driving test**.

Here’s what it does step by step:

1. **Asks for the user’s age**
```python
age = input("Enter your age?\n ")
   age = int(age)
```

   `input()` gets the age as text, so `int(age)` converts it into a number.

2. **Checks if the user is old enough**
```python
if age > 17:
```

   If the age is greater than `17`, the person is allowed to take the driver test.

3. **If the user is younger than 18**
```python
else:
       print("you are not eligible to take a driver test")
       exit()
```

   The program prints a message and stops using `exit()`.

4. **Asks if the user passed the driver test**
```python
driver_test = input("Do you passed the driver test?\n ")
```


5. **Checks the answer**
```python
if driver_test == "yes":
```

   If the user types `"yes"`, the program says they are eligible to drive.

```python
elif driver_test == "no":
```

   If the user types `"no"`, the program says they need to pass the test.

```python
else:
```

   If the user types anything other than `"yes"` or `"no"`, the program asks them to enter a valid answer.

In simple words:  
**If the person is 18 or older and passed the driving test, they can drive.**
