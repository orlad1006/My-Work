# Title: Student.py
#Author: Orla Dowling
#Task: Write a function that prints out a menu of commands we can perform, ie add,
#view and quit. The function should return what the user chose.
#Test the function. We don’t need to worry about error handling yet

'''
def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice
#test the function
choice = displayMenu()
print(f"you chose { choice }")'''

#part 3 of student.py
'''
def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice
def doAdd():
 # we fill this in later
 print("in adding")
def doView():
 # we fill this in later
 print("in viewing")
#main program
choice = displayMenu()
while(choice != 'q'):
 # we could do this with lambda functions
 # I am keeping this basic for the moment
    if choice == 'a':
         doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu() 
    '''

#party 4 of student.py
'''
students= []
def readModules():
    return []
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)
#test
doAdd(students)
doAdd(students)
print (students)'''

#part 5:
'''
def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules'''
'''
#Part 6 
# the array we store everything in
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def readModules():
 modules = []
 moduleName = input("\tEnter the first Module name (blank to quit) :").strip()

 while moduleName != "":
    module = {}
    module["name"]= moduleName
    # I am not doing error handling
    module["grade"]=int(input("\t\tEnter grade:"))
    modules.append(module)
    # now read the next module name
    moduleName = input("\tEnter next module name (blank to quit) :").strip()
 return modules


def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print(f"\t{ module['name']} \t{ module['grade']}")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);

#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda functions
     # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
         print("\n\nplease select either a,v or q")
choice=displayMenu()

'''




#Extra

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def doAdd(students):
    print("do add")

def doView(students):
    print("do View")

def doNothing(dumby):
    pass

#the dict that maps a letter to function
choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing # q is a valid choice
}

#main program
Students = []
choice = displayMenu()
while(choice != 'q'):
    if choice in choiceMap:
     # run the function
        choiceMap[choice]('students')
    else: # use did not enter something valid
        print("\n\nplease select either a,v or q")

    choice=displayMenu()