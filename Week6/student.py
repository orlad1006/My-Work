# Title: Student.py
#Author: Orla Dowling
#Task: Write a function that prints out a menu of commands we can perform, ie add,
#view and quit. The function should return what the user chose.
#Test the function. We don’t need to worry about error handling yet


def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice
#test the function
choice = displayMenu()
print(f"you chose { choice }")
