#creating a list. lists are written with square brackets.
thislist = ["apple", "banana", "cherry"]
print("printing the list")
print(thislist)
#accessing list elements
print(thislist[0])
print(thislist[1])
print(thislist[2])
#chaning the value of position 1
thislist[1] = "blackcurrant"
print(thislist)
#length of list
print("Length of list is: ")
print(len(thislist))
#add items to end of list
thislist.append("orange")
print(thislist)
#add items at specific postion
thislist.insert(2, "melon")
print(thislist)
#remove item from list
thislist.remove("cherry")
print(thislist)
#You cannot copy a list simply by list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2. 
#There are ways to make a copy, one way is to use the built-in List method copy(). 
myCopiedlist = thislist.copy()
print("Printing the new copied list mylist")
print(myCopiedlist)
# Another way to make a copy is to use the built-in method list()
myAnotherList = list(thislist)
print("Printing the new another list mylist")
print(myAnotherList)
#The clear() method empties the list:
thislist.clear()
print(thislist)
# creating a new list with list constructor
constructedList = list(("pineapple", "mango", "badam")) # note the double round-brackets
print(constructedList)
#del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#del can also remove the entire list
del thislist