# grade.py
#Author: Orla Dowling

# This program reads in
# a students percentage
# and prints out the
# corresponding grade

percentage = float(input( "Enter the percentage: "))
#print(percentage)

# be careful with ands and ors
if percentage <0 or percentage >100:
# later we will show error handling
# this should really throw an error
  print("Please enter a number between 0 and 100")
elif percentage <40: 
  print("Fail")
elif percentage <50:
  print("Pass")
elif percentage <60:
  print("Merit")
elif percentage <70:
  print("Merit2")
else:
  print("Distinction")
  