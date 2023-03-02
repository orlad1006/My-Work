#labs3.2.convert.py
#Author: Orla Dowling
# write a program that takes in a float amount in dollars
# outputs the absolute amount in cents
# issue: may be a minus in front of the amount


amount = float(input("Please enter an amount: "))

absolute_value = abs(amount)

converted_amount = int(absolute_value*100)

print("That amount in cent is: {}".format(converted_amount))
