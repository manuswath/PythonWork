def concat(*args, sep="/"):
    return sep.join(args)

x = concat("earth", "mars", "venus")
y = concat("earth", "mars", "venus", sep=".")

print(x)
print(y)