import sys

if len (sys.argv) != 3 :
    print ("Usage: python commandLineArgument.py $First_Name $Lasst_name")
    sys.exit (1)

fname = sys.argv[1]
lname = sys.argv[2]
print("Hello: "+fname+" "+lname)