#is_even.py
#Author: Orla Dowling

# write a program that asks the user to enter in a number,  
#the program will tell the user if the number is odd or even

number = int(input(" Please enter an integer here:  "))

if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")

    

