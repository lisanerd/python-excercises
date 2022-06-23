
def appearing_n(numbers:list[int]):
    uniques = set(numbers)
    # print(f"{uniques=}")
    for n in uniques:
        # print(f"{n}")
        appearances = numbers.count(n)
        if n == appearances:
            return True
    return False


answer = appearing_n(numbers=[2,2,3,4,5,2,3,4,3,5,5,5,5,3])

print(f"Answer = {answer}")