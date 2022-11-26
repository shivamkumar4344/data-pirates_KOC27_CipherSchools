# Makng Magic square matrix
a = []
for i in range(4):
    b = []
    for j in range(4):
        j = int(input("Enter the number:-"))
        b.append(j)
    a.append(b)
print("MATRIX IS==")
for i in range(4):
    for j in range(4):
        print(a[i][j],end = " ")
    print()
sum_diagonal1 = 0
sum_diagonal2 = 0
for i in range(4):
    for j in range(4):
        if i == j:
            sum_diagonal1 += a[i][j]
        if i + j == 3-1:
            sum_diagonal2 += a[i][j]
if  sum_diagonal1 != sum_diagonal2:
    f = 1
else:
    for i in range(4):
        sum_row = 0
        sum_coloumn = 0
        for j in range(4):
            sum_row += a[i][j]
            sum_coloumn += a[i][j]
        if sum_row != sum_diagonal1:
            f = 1
        elif sum_coloumn != sum_diagonal1:
            f = 1
        else:
            f = 0
if f == 0:
    print("MATRIX IS MAGIC SQUARE")
else:
    print("MATRIX IS NOT MAGIC SQUARE")
            
        
