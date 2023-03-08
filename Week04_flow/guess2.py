# guess2.py
# Author: Orla Dowling

#modift guess1 so program tells user if guess is too high or too low


number_to_guess = 30 

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    if guess < number_to_guess:
      print("too low")
    else: 
      print ("too high")
    guess = int(input("Please guess again"))

print ("Well done! Yes the number was", number_to_guess)


