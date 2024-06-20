r = int(input("enter rows"))
c = int(input("enter columns"))
A = []
for i in range(r) :
    x = []
    for j in range(c) :
        x.append(int(input()))
    A.append(x)
for i in range(r) :
    for j in range(c) :
              print(A[i][j],end=" ")
    print()
    for i in range(len(A)):
        for j in range(len(A[0])):
            c[i][j] = A[i][j] + b[i][j]