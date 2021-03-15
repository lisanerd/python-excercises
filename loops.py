

# "for" loops
primes = [3, 13, 41, 71]
for prime in primes:
    print(prime)

# range function returns a new list with numbers of that specified range; xrange returns an iterator, which is more efficient
for x in range(10):
    print(x)

for x in range(1, 7):
    print(x)

for x in range(2, 14, 3):
    print(x)

# "while" loops repeat as long as a certain boolean* condition is met. *(see Operators_Boolean_in_is_not.py)
count = 3
while count < 18:
    print(count)
    count += 1

# "break" and "continue" statements
    # "break" is used to exit a for loop or a while loop
    # "continue" is used to skip the current block, and return to the "for" or "while" statement.
count = 3
while True:
    print(count)
    count+=1
    if count >= 11:
        break
    
for x in range(21):
    if x % 2 == 0:
        continue
    print(x)

# The "else" clause can be used for loops. They are skipped if there is a break statement before it, but it is used even if there is a continue statement before it.
count=0
while(count<9):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

for i in range(1, 10):
    if(i%7==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")