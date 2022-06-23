

# first = input("First number: ")
# second = input("Second number: ")
# product = int(first) * int(second)
# print("Sum: " + str(product))



weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper == "K":
    converted = weight / 0.45
    print("Weight in Lbs is: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kg is: " + str(converted))