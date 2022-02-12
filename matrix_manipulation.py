import numpy as np

def take_min(element1, element2):

    def matrix_min(M1, M2):
        dimension = M1.shape
        M = []
        for i in range(dimension[0]):
            r = []
            for j in range(dimension[1]):
                if M1[i][j] < M2[i][j]:
                    r.append(M1[i][j])
                else:
                    r.append(M2[i][j])
            M.append(r)
        return np.array(M)


    def matrice_int_min(M1, i1):
        dimension = M1.shape
        M = []
        for i in range(dimension[0]):
            r = []
            for j in range(dimension[1]):
                if M1[i][j] < i1:
                    r.append(M1[i][j])
                else:
                    r.append(i1)
            M.append(r)
        return np.array(M)


    def int_int(i1, i2):
        if i1 < i2:
            return i1
        else:
            return i2

    try:
        len(element1)
    except TypeError:
        i1 = element1
        try:
            len(element2)
        except TypeError:
            i2 = element2
            return int_int(i1,i2)
        else:
            M1 = element2
            return matrice_int_min(M1, i1)

    else:
        M1 = element1
        try:
            len(element2)
        except TypeError:
            i2 = element2
            return matrice_int_min(M1, i2)
        else:
            M2 = element2
            return matrix_min(M1, M2)

