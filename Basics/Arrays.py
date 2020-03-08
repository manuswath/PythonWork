#initialize and print array
cars = ["Ford", "Volvo", "BMW"]
print(cars)

#access array at index value
x = cars[0]
print(x)

#setting value at index value
cars[0] = "Toyota"
print(cars)

#length of array
x = len(cars)
print(x)

#looping thru array
for x in cars:
  print(x)

#adding element to array
cars.append("Honda")
print(cars)

#removing element from array
cars.pop(1)
print(cars)
cars.remove("BMW")
print(cars)

