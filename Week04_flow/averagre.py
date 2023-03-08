#average.py
#Author: Orla Dowling

#write a program taht keeps reading the number until the user enters 0
#the program should append each of them to a list
#Print out each of the numbers entered and the average of them (use a list)

numbers = []
# first number then we check if it is 0 in the while loop

number = int(input("enter number (0 to quit) "))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number = int(input(" enter another (0 to quit)"))

for value in numbers:
    print (value)

# i want average to be a float

average = float(sum(numbers))/len(numbers)
print(f"the average is {average}")
