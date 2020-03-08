import datetime

def invokeFunctionA():
    x = datetime.datetime.now()
    print(x)
    print("Inside function A: ")

def invokeFunctionB():
    y = datetime.datetime.now()
    print(y)
    print("Inside function B: ")

def invokeFunctionC():
    z = datetime.datetime.now()
    print(z)
    print("Inside function C: ")

#call functions one after the other
invokeFunctionA()
invokeFunctionB()
invokeFunctionC()