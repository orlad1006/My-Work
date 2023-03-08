# guess.py
# Author: Orla Dowling

#write a program that prompts the user to guess a number, the program should keep prompting the user to 
#guess the number until  the user get the right one


number_to_guess = 30 

guess = int(input("Please guess the number:"))
while guess != number_to_guess:C
    print ("Wrong")
    guess = int(input("Please guess again: "))

    print ("Well done! Yes the numbwe was", number_to_guess)


