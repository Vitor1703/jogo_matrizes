matrixOne = [[1, 12, 45], [58, 524, 78], [1, 2, 3], [45, 456, 8]]
matrixTwo = [[0, 1, 2], [85, 1, 74], [27, 63, 21], [25, 47, 962]]

matrixTrhee = []
for l in range(4):
    line = []
    for c in range(3):
        if matrixOne[l][c] > matrixTwo[l][c]:
            line.append(matrixOne[l][c])
        else:
            line.append(matrixTwo[l][c])
    matrixTrhee.append(line)

print(matrixTrhee)