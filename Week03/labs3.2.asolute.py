# labs3.2.absolute.py
#Author: Orla Dowling
#Give the absolute value of a number
# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# So I am casting the input to a float

number = float(input("Enter the number: "))
absolute_value = abs(number)

print('The absolute value of {} is {}'.format(number,absolute_value))

