# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist


f = open("writefile.txt", "a")
f.write("File has some content!")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("writefile.txt", "r")
print(f.read())

#create file
f = open("myfile.txt", "x")

#create another file
f = open("mytext.txt", "w")