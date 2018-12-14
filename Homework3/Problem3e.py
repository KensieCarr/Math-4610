def crossProduct(vectorOne, vectorTwo):
    vectorFinal = []
    vectorFinal.append(vectorOne[1]*vectorTwo[2]-vectorOne[2]*vectorTwo[1])
    vectorFinal.append(vectorOne[2]*vectorTwo[0]-vectorOne[0]*vectorTwo[2])
    vectorFinal.append(vectorOne[0]*vectorTwo[1]-vectorOne[1]*vectorTwo[0])
    return vectorFinal


if __name__ == '__main__':
    from utils import inputVectors, vStr
    vectors = inputVectors()
    print("{0} X {1} = {2}".format(vStr(vectors[0]), vStr(vectors[1]), vStr(crossProduct(vectors[0], vectors[1]))))
