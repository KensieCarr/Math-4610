def subtractVectors(vectorOne, vectorTwo):
    vectorFinal = []
    for i in range(0,len(vectorOne)):
        vectorFinal.append(vectorOne[i] - vectorTwo[i])
    return(vectorFinal)

if __name__ == '__main__':
    from utils import inputVectors
    vectors = inputVectors()
    print(vectors[0], "-", vectors[1], "=", subtractVectors(vectors[0], vectors[1]))