#labs3.2.rounds.py
#Author: Orla Dowling
#this program rounds a number... input float output int
# Be careful of round, it rounds to the nearest even number 
# eg 4.5 rounds to 4,
# but 5.5  rounds to 6,
# so do not use it accuracy is essential

number_to_round = float(input("Enter a float number: "))
rounded_number = round(number_to_round)

print('{} rounded is {}'.format(number_to_round,rounded_number))

