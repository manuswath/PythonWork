#Simple Lambda anonymous function
x = lambda a: a + 10
print(x(5))

#Lambda that takes args
x = lambda a, b: a * b
print(x(5, 6))

#Lambda with more args
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

#returning lambda function
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))



