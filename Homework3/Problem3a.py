import numpy as np

def inputVectors():
    sizeOfVector = int(input("Size of vector: "))
    vectorOne = []
    vectorTwo = []
    for i in range(0,sizeOfVector):
        vectorOne.append(int(input("value: ")))
    for i in range(0,sizeOfVector):
        vectorTwo.append(int(input("value: ")))
    return (vectorOne, vectorTwo)

vectors = inputVectors()

def addVectors(vectorOne, vectorTwo):
    vectorFinal = []
    for i in range(0,len(vectorOne)):
        vectorFinal.append(vectorOne[i] + vectorTwo[i])
    return(vectorFinal)

print(vectors[0], "+", vectors[1], "=", addVectors(vectors[0], vectors[1]))
