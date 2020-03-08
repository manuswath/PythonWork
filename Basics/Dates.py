import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

#Creating date objects
y = datetime.datetime(2020, 5, 17)
print(y)

z = datetime.datetime(2018, 6, 1)

print(z.strftime("%B"))
