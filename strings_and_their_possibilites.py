string = "hello! my name is lisa!"

# the lines that follow will all be based on the string listed above

print(len(string))
# this provides the length of my "string"

print(string.index("a"))
# this tells me the index position of the given letter, a

print(string.count("l"))
print(string.count("e"))
# these two lines are counting the number of corresponding indexes (one is l and one is e) in my "string"

print(string[5:11])
print(string[5:11:1])
# the two lines above have the same outcome since I am telling them to go from index 5 to index 11 while skipping by 1, which will give the same result
print(string[5:11:3])
# this line will only hold index 5, 8, and 11 because it is skipping by 3's
print(string[::-1])
# by leaving out the first two values, the outcome of this line is that it will write the my "string" backwards, since I am telling it to skip count by -1, so starting at the end of the line

print(string.upper())
# as you can interpret, this will write my "string" in upper case letters
print(string.lower())
# you can  interpret as well that this will write my "string" in lower case letters (which will be identical to my "string" since it was originally lower case)

print(string.startswith("hello"))
print(string.startswith("y"))
# these two lines cause a True or Flase statement, according to whether or not my "string" begins with the given index
print(string.endswith("!"))
print(string.endswith("a"))
# these two lines also cause a True or Flase statement, but now according to whether or not my "string" ends with the given index