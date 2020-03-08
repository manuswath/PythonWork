f = open("demofile.txt", "r")
print(f.read())
f.close()
print("-----------------------------------------------------")
#Read parts of the file and display return the first 5 chars
f = open("demofile.txt", "r")
print(f.read(5))
f.close()
print("-----------------------------------------------------")
#read lines of file
f = open("demofile.txt", "r")
print(f.readline())
f.close()
print("-----------------------------------------------------")
#loop thru the lines of the file
f = open("demofile.txt", "r")
for x in f:
  print(x)
f.close()
print("-----------------------------------------------------")
