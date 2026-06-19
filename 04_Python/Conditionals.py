
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