matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
print(matrix)

#adding one more row in new var from matrix
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)