# labs_div.py
#Author:Orla Dowling
#program that reads in two numbers 
#outputs the integer answer and the remainder

x = int(input('Enter first number: '))
y = int(input('Enter the number you wantto divide by: '))
answer = int(x//y) #gives the int division
remainder = x%y # gives the remainder

print('{} divided by {} is {} with remainder {}'.format(x,y,answer,remainder))

