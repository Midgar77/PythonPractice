#!/usr/bin/python

#Shows the different uses of functions and arguments.




#Python functions are "pass by reference" which means that if you change an argument within the function, that argument will be changed outside the function

# Takes input list argument and appends [1,2,3,4] to it. Input list argument is changed outside the function as well due to reference.
def changeList(myList):
   myList.append([1,2,3,4]);
   #Will print out [10, 20, 30, 40,[1, 2, 3, 4]]
   print "Values inside the function: ", myList
   return

#
mylist = [10,20,30,40];
changeList(myList);
#Will still print out [10, 20, 30, 40,[1, 2, 3, 4]] because of reference
print "Values outside the function: ", mylist
