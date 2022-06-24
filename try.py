
from math import sqrt

print(7/3)
print(9/3)
print(7//3)
print(9//3)
print(7%3)
print(9%3)

def is_prime(number:int):
    for test in range (2, int(sqrt(number)) + 1):
        if number%test == 0:
            if number > test:
                return False
    # if number%2 == 0:
    #     return False
    # if number%3 == 0:
    #     if number > 3:
    #         return False
    # if number%4 == 0:
    #     if number > 4:
    #         return False

    
    return True




for i in range(2, 1000):
    ret = is_prime(i)
    print(f"{i} is prime: {ret}" )

print(len(str(35742549198872617291353508656626642567)))
is_prime(35742549198872617291353508656626642567)