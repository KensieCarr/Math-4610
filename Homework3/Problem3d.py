def dotProduct(vectorOne, vectorTwo):
    product = 0
    for i in range(0,len(vectorOne)):
        product += vectorOne[i] * vectorTwo[i]
    return product

if __name__ == '__main__':
    from utils import inputVectors, vStr
    vectors = inputVectors()
    print("{0} * {1} = {2}".format(vStr(vectors[0]), vStr(vectors[1]), dotProduct(vectors[0], vectors[1])))