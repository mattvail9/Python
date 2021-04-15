from fractions import Fraction
def gcd(x, y):
    def gcd1(x, y):
        if y == 0:
            return x
        return gcd1(y, x%y)
    return gcd1(abs(x), abs(y))

def simplify(x, y):
    g = gcd(x, y)
    return Fraction(int(x/g), int(y/g))

def lcm(x, y):
    return int(x*y/gcd(x,y))

def transform(mat):
    sum_list = list(map(sum, mat))
    bool_indices = list(map(lambda x: x == 0, sum_list))
    indices = set([i for i, x in enumerate(bool_indices) if x])
    new_mat = []
    for i in range(len(mat)):
        new_mat.append(list(map(lambda x: Fraction(0, 1) if(sum_list[i] == 0) else simplify(x, sum_list[i]), mat[i])))
    transform_mat = []
    zeros_mat = []
    for i in range(len(new_mat)):
        if i not in indices:
            transform_mat.append(new_mat[i])
        else:
            zeros_mat.append(new_mat[i])
    transform_mat.extend(zeros_mat)
    tmat = []
    for i in range(len(transform_mat)):
        tmat.append([])
        extend_mat = []
        for j in range(len(transform_mat)):
            if j not in indices:
                tmat[i].append(transform_mat[i][j])
            else:
                extend_mat.append(transform_mat[i][j])
        tmat[i].extend(extend_mat)
    return [tmat, len(zeros_mat)]

def copy_mat(mat):
    cmat = []
    for i in range(len(mat)):
        cmat.append([])
        for j in range(len(mat[i])):
            cmat[i].append(Fraction(mat[i][j].numerator, mat[i][j].denominator))
    return cmat

def gauss_elmination(m, values):
    mat = copy_mat(m)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        mat[i], mat[index] = mat[index], mat[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i]/mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        index = len(mat) -1 -i
        end = len(mat) - 1
        while end > index:
            values[index] -= mat[index][end] * res[end]
            end -= 1
        res[index] = values[index]/mat[index][index]
    return res

def transpose(mat):
    tmat = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == 0:
                tmat.append([])
            tmat[j].append(mat[i][j])
    return tmat

def inverse(mat):
    tmat = transpose(mat)
    mat_inv = []
    for i in range(len(tmat)):
        values = [Fraction(int(i==j), 1) for j in range(len(mat))]
        mat_inv.append(gauss_elmination(tmat, values))
    return mat_inv

def mat_mult(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res
    
def splitQR(mat, lengthR):
    lengthQ = len(mat) - lengthR
    Q = []
    R = []
    for i in range(lengthQ):
        Q.append([int(i==j)-mat[i][j] for j in range(lengthQ)])
        R.append(mat[i][lengthQ:])
    return [Q, R]
    
def solution(mat):
    res = transform(mat)
    if res[1] == len(mat):
        return [1, 1]
    Q, R = splitQR(*res)
    inv = inverse(Q)
    res = mat_mult(inv, R)
    row = res[0]
    l = 1
    for item in row:
        l = lcm(l, item.denominator)
    res = list(map(lambda x: int(x.numerator*l/x.denominator), row))
    res.append(l)
    return res
    #row_sums = [sum(x) for x in matrix] 
    '''print(transform(matrix))
    ordered_matrix = []
    identity_index = 0
    for i in range(len(matrix)):
        if sum(matrix[i]) > 0:
            ordered_matrix.append(matrix[i])
        else:
            ordered_matrix.insert(identity_index, matrix[i])
            identity_index += 1
    if(ordered_matrix[1] == len(matrix)):
        return [1, 1]
        
    #sums = [sum(x) for x in ordered_matrix]
    #extract q
    q = [[i for i in row[identity_index:]] for row in ordered_matrix[identity_index:]]
    #create identity matrix
    identity_matrix = [[int(x==y) for x in range(len(q))] for y in range(len(q))]
    #extraxt R
    r = [[i for i in row[:identity_index]] for row in ordered_matrix[identity_index:]]
'''
    #I-Q
    '''for i in range(len(identity_matrix)):
        for j in range(len(q)):
            q[i][j] = identity_matrix[i][j] - (q[i][j] / sums[i+identity_index]) if q[i][j] > 0 else 0
    
    new_matrix = matmult(inverse(q), r)
    
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            frac = Fraction(new_matrix[i][j])
            print(frac.numerator,'\\',frac.denominator)
        print()'''

def matmult(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res
    
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                print("MATRIX NOT INVERTIBLE")
                return -1
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret
    
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
