```python
#name = "jamal"

#for letter in name :
    #print(letter)


cars = ["Audi" , "toyota" , "BMW"]

for car in cars:
    print(car)
```


# Understanding the `cars` Constant

## Summary

The `cars` constant is a list that stores three string values representing car brand names. It serves as a data container that is then iterated over in a `for` loop to print each car brand individually.

## Key Details

- **Definition**: `cars = ["Audi" , "toyota" , "BMW"]` creates a list with three car brand names
- **Data Type**: A list containing string elements
- **Purpose**: Provides a collection of car names to be processed by the loop

## How It's Used

The `cars` constant is used directly in the `for` loop on line 9:

```python
for car in cars:
    print(car)
```

In this context:
- The `for` loop iterates through each element in the `cars` list
- On each iteration, the variable `car` temporarily holds the current element
- The `print(car)` statement outputs each car brand name, one per line

## Output

Running this code produces:
```
Audi
toyota
BMW
```

The loop accesses each item in the `cars` list sequentially and prints it to the console. This demonstrates how a constant list can be reused efficiently without manually writing multiple print statements.
