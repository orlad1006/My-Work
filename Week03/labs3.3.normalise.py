# labs3.3.normalise.py
# Author: Orla Dowling
#This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string
# and the normalised one
#

raw_string = input("Please enter a string")

normalised_string = raw_string.strip().lower()

lenght_of_raw_string = len(raw_string)
lenght_of_normalised_string = len(normalised_string)

print(f"That string normalised is : {normalised_string}")
print(f"We reduced the input string from {lenght_of_raw_string} to {lenght_of_normalised_string} characters")

