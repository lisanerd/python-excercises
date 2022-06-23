
# for i in range(4):
#     print(i)


# people = ["Lisa", "Maya", "Gael", "Adeline"]

# i = 0
# for p in people:
#     print("Hi " + p)
#     print(f"The custumer id of {p} is {i}")
#     i += 1

# for j,p in enumerate(people):
#     print(f"The custumer id of {p} is {j}") 


def number_contains(number:int, digit_to_find:int):
    #     "2"  in  "126"
    if str(digit_to_find) in str(number):
        return True
    return False

n = 0
for xyz in range(101):
    if number_contains(number=xyz, digit_to_find=2):
        print(f"{xyz} contains a 2")
        n += 1
print(f"There were a total of {n} number containing a 2")


def number_counts(number:int, digit_to_count:int):
    total = 0
    for c in str(number):
        if str(digit_to_count) == c:
            total += 1
        # print(total)
    return total

total_number = 0
for xyz in range(1000000):
    ret = number_counts(number=xyz, digit_to_count=2)
    total_number += ret
print(f"I counted {total_number} digits of 2")
