#!/usr/bin/python

#Shows the different uses of functions and arguments.



#Python functions are "pass by reference" which means that if you change an argument within the function, that argument will be changed outside the function

# Takes input list argument and appends [1,2,3,4] to it. Input list argument is changed outside the function as well due to reference.
def changeList(myList):
   myList.append([1,2,3,4]);
   #Will print out [10, 20, 30, 40,[1, 2, 3, 4]]
   print "Values inside the function: ", myList
   return


#Main code
mylist = [10,20,30,40];
changeList(myList);
#Will still print out [10, 20, 30, 40,[1, 2, 3, 4]] because of reference
print "Values outside the function: ", mylist


#----------------------------------------------------------------------------------



#There are 4 different types of Python function parameters:
#  -Required arguments
#  -Keyword arguments
#  -Default Arguments
#  -Variable-length arguments


# 1. Required arguments are the simplest.

#Takes in a str argument and prints it. If a str argument is not passed, a TypeError is thrown.
def printString(str):
   print str
   return;

#Below throws a TypeError because it is calling printString without any argument.
printString()



# 2. Keyword arguments allow declaration of a variable inside the function call.

#Takes in a str argument and prints it.
def printString(str):
   print str
   return;

#Notice how str wasn't declared first and then passed when calling printString, rather we assign a value to the argument as it is passed
printString(str = "Hello world!")


