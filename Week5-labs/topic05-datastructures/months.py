# Months of Year
#Author: Orla Dowling
#Task: Create a tuple that stores the months of the year, from that tuple create
#another tuple with just the summer months (May, June, July), print out the
#summer months one at a time.

months_of_year = ("January",
                  "Feburary", 
                  "March", 
                  "April",
                   "May", 
                   "June",
                    "July", 
                    "August", 
                    "September",
                    "October",
                    "November",
                    "December")


#summer_months = ("May","June","July")

#x,y,z = summer_months
#print(x)
#print(y)
#print(z)

summer = months_of_year[4:7]

for month in summer:
    print (month)



