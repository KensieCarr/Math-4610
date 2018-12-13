def inputVectors():
    sizeOfVector = int(input("Size of vector: "))
    vectorOne = []
    vectorTwo = []
    for i in range(0,sizeOfVector):
        vectorOne.append(int(input("value: ")))
    for i in range(0,sizeOfVector):
        vectorTwo.append(int(input("value: ")))
    return (vectorOne, vectorTwo)

def inputVector():
    sizeOfVector = int(input("Size of vector: "))
    vector = []
    for i in range(0,sizeOfVector):
        vector.append(int(input("value: ")))
    return vector
    