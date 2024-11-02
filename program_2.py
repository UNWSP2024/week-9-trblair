# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random
def randnum():
    count = int(input("How many random numbers would you like to generate?\n"))
    if count < 0:
        count=0
    elif count > 1000:
        count=1000
    with open("random numbers.txt","w") as f:
        for x in range(count):
            gennum=random.randint(1,500)
            f.write(str(gennum))
            f.write("\n")

randnum()
