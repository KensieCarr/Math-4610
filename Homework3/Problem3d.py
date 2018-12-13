def dotProduct(vectorOne, vectorTwo):
    product = 0
    for i in range(0,len(vectorOne)):
        product += vectorOne[i] * vectorTwo[i]
    return product

if __name__ == '__main__':
    from utils import inputVectors
    vectors = inputVectors()
    print(vectors[0], "*", vectors[1], "=", dotProduct(vectors[0], vectors[1]))