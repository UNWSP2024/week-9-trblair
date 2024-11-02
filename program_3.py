# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################
    # Add your code here #
    ######################
    with open('numbers.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace("\n", ",") for line in lines]
    with open('numbers.txt', 'w') as f:
        f.writelines(lines)
    numbers= open("numbers.txt","r")
    stringlist=(numbers.read()).split(",")
    intlist=[]
    for x in stringlist:
        intlist.append(int(x))

        

    print(sum(intlist))
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
