def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
#uses a lambda expression to return a function.
print(f)