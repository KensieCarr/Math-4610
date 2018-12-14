def addMatrices(m1, m2):
    if len(m1) != len(m2):
        raise ValueError("Matrices must be the same size")
    return [x + y for x, y in zip(m1, m2)]


if __name__ == '__main__':
    from utils import inputMatrices, mStr
    matrices = inputMatrices()
    r,c = matrices[2], matrices[3]
    print("{} +\n{} =\n{}".format(mStr(matrices[0], r, c), mStr(matrices[1], r, c), mStr(addMatrices(matrices[0], matrices[1]), r, c)))
