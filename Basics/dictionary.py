# dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, 
# and they have keys and values.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# access the items of a dictionary by referring to its key name, inside square brackets
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)
#change the value of a specific item by referring to its key name:
thisdict["year"] = 2018
print(thisdict)
#loop through a dictionary by using a for loop and print all key-names
for x in thisdict:
  print(x)
#loop through a dictionary by using a for loop and print all values
for x in thisdict:
  print(thisdict[x])
#one more to return all values
for x in thisdict.values():
  print(x)
#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)
#Check if Key Exists
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#To determine how many items (key-value pairs) a dictionary has
print(len(thisdict))
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["color"] = "red"
print(thisdict)
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
mydict = thisdict.copy()
print(mydict)
#Another way to make a copy is to use the built-in method dict().
constructedDict = dict(thisdict)
print(constructedDict)
constuctorDict = dict(brand="Ford", model="Mustang", year=1964) # note that keywords are not string literals. note the use of equals rather than colon for the assignment
print(constuctorDict)
#remove items from a dictionary:
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["year"]
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.