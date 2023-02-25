#sub.py
#Author: Orla Dowling
#program to subtract one number from the other
#input reads in a string so we have to convert it to a number
#so we can do mathematical operations

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = x-y
print ("{} minus {} is {} ".format(x,y,answer))
