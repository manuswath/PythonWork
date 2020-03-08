import os
#you can only remove empty folders
if os.path.exists("myfolder"):
 os.rmdir("myfolder")
else:
  print("The folder does not exist")
