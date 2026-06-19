
cars = ["audi\n", "toyota\n", "bmw\n"]
adjectives = ["(fast)" , "(expensive)\n"]

for car in cars:
    print(car + " | ")
    for adjective in adjectives:
        print(" - " + adjective)