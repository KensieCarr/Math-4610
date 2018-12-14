def scalarVecMultiply(scalar, vector):
    vectorFinal = []
    for i in range(0,len(vector)):
        vectorFinal.append(vector[i] * scalar)
    return(vectorFinal)

if __name__ == '__main__':
    from utils import inputVector, vStr
    scalar = input("Input scalar multplier: ")
    vector = inputVector()
    print("{} * {} = {}".format(scalar, vStr(vector), vStr(scalarVecMultiply(scalar, vector))))