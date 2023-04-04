# queue lists
#Author: Orla Dowling
#Task: Create a program that puts 10 random numbers into a queue(list), the
#program should then output all the values in the queue, then take the
#numbers from the queue one at a time, print it and the current numbers still
#in the queue. (the command pop(0) takes the first element out of a list)


import random
queue = []
numberOfNumbers=10
rangeTo=100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))
print (f"queue is {queue}")
while len(queue) != 0:

    currentNumber = queue.pop(0)


print ("current Number is {currentNumber} and the queue is {queue} ")


print ("the queue is now empty")


