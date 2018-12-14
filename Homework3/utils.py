def inputVectors():
    sizeOfVector = int(input("Size of vector: "))
    vectorOne = []
    vectorTwo = []
    for i in range(0,sizeOfVector):
        vectorOne.append(float(input("value: ")))
    for i in range(0,sizeOfVector):
        vectorTwo.append(float(input("value: ")))
    return (vectorOne, vectorTwo)

def inputVector():
    sizeOfVector = float(input("Size of vector: "))
    vector = []
    for i in range(0,sizeOfVector):
        vector.append(float(input("value: ")))
    return vector
    

def vStr(vector):
    return '(' + ', '.join("{0}".format(n) for n in vector) + ')'

def inputMatrices():
    sizeOfMatrix = (int(input("Row Size: ")), int(input("Column Size: ")))
    matrixOne = []
    matrixTwo = []
    print("Matrix 1\n~~~~~~~~")
    for i in range(0,sizeOfMatrix[0]):
        for j in range(0, sizeOfMatrix[1]):
            matrixOne.append(float(input("value for r:{},c:{}: ".format(i, j))))
    print("Matrix 2\n~~~~~~~~")
    for i in range(0,sizeOfMatrix[0]):
        for j in range(0, sizeOfMatrix[1]):
            matrixTwo.append(float(input("value for r:{},c:{}: ".format(i, j))))
    return (matrixOne, matrixTwo, sizeOfMatrix[0], sizeOfMatrix[1])

def mStr(matrix, r, c):
    if (len(matrix) % r != 0) or (len(matrix) % c != 0):
        raise ValueError("Rows or Columns is not correct")
    ret = ''
    for i in range(r):
        for j in range(c):
            ret += "{} ".format(matrix[i+j])
        ret += "\n"
    return ret