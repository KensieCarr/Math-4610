def addVectors(vectorOne, vectorTwo):
    vectorFinal = []
    for i in range(0,len(vectorOne)):
        vectorFinal.append(vectorOne[i] + vectorTwo[i])
    return(vectorFinal)

if __name__ == '__main__':
    from utils import inputVectors, vStr
    vectors = inputVectors()
    print("{} + {} = {}".format(vStr(vectors[0]), vStr(vectors[1]), vStr(addVectors(vectors[0], vectors[1]))))

