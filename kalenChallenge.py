

def appearing_n(numbers:list[int]) -> list[int]:
    match = 0
    uniques = set(numbers)
    # print(f"{uniques=}")
    for n in uniques:
        # print(f"{n}")
        appearances = numbers.count(n)
        if n == appearances:
            match += 1
            numbers = [i for i in numbers if i != n]

    numbers.sort()
    return numbers

answer = appearing_n(numbers=[9,2,2,3,4,5,3,4,4,3,5,5,4,5,5,3, 6, 6])

print(f"Answer = {answer}")