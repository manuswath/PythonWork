import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")

#Check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a list containing every occurrence of "ai":
x = re.findall("ai", txt)
print(x)

#one more search
str = "The rain in Spain"
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start()) 

#Split the string at every white-space character:
str = "The rain in Spain"
x = re.split("\s", str)
print(x)

#one more split after the first occurence
#Split the string at the first white-space character:
str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)

#Replace every white-space character with the number 9:
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

#Replace the first two occurrences of a white-space character with the digit 9:
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)

#Search for an upper case "S" character in the beginning of a word, and print its position:
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

#The string property returns the search string:
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)

#Search for an upper case "S" character in the beginning of a word, and print the word:
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())
