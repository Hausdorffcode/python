def maxtriAdd(m, n):
    rowsm = len(m)
    colsm = len(m[0])
    rowsn = len(n)
    colsn = len(n[0])
    if rowsm == rowsn and colsm == colsn:
        answer = []
        for i in range(rowsm):
            oneRow = []
            for j in range(colsm):
                oneRow.append(m[i][j] + n[i][j])
            answer.append(oneRow)
        return answer
    else:
        print "invaild"
        return -1

m = [[1,2,3], [4,5,6], [7,8,9]]
n = [[0,1,2], [1,0,2], [2,1,0]]

print maxtriAdd(m, n)

def vectorMul(a,b):
    answer = 0
    lenm = len(a)
    lenn = len(b)
    if lenm == lenn:
        for i in range(lenn):
                answer += (a[i] * b[i])
        return answer
    else:
        print 'invalid'
        return -2

print vectorMul([1,2,3], [0,1,2])

def maxtriMul(m, n):
    rowsm = len(m)
    colsm = len(m[0])
    rowsn = len(n)
    colsn = len(n[0])
    if colsm == rowsn:
        answer = []
        for i in range(rowsm):
            oneRow = []
            for j in range(colsn):
                oneRow.append(vectorMul(m[i], [n[a][j] for a in range(rowsn)]))
            answer.append(oneRow)
        return answer
    else:
        print 'invalid'
        return -1

print maxtriMul(m, n)
