class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    #calling base class's init  
    Person.__init__(self, fname, lname)
    #adding extra functionality
    self.graduationyear = 2019

  #adding extra method
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Tyson")
x.printname()
print(x.graduationyear)
x.welcome()
