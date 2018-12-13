def scalarVecMultiply(scalar, vector):
    vectorFinal = []
    for i in range(0,len(vector)):
        vectorFinal.append(vector[i] * scalar)
    return(vectorFinal)

if __name__ == '__main__':
    from utils import inputVector
    scalar = input("Input scalar multplier: ")
    vector = inputVector()
    print(scalar, "*", vector, "=", scalarVecMultiply(scalar, vector))