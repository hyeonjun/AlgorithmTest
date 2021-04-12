def MySolution(A): # 60%
    zero = []
    one = []
    for i in range(len(A)):
        if(A[i] == 0): zero.append(i)
        else: one.append(i)
    check = 0
    for i in zero:
        for j in one:
            if(i < j):
                check+=1
                if(check > 1000000000):
                    return -1
    return check


print(MySolution([0,1,0,1,1]))

def MySolution2(A):
    check = 0
    count = 0
    for i in range(len(A)):
        if(A[i] == 0): check+=1
        else:
            count+= 1*check
            if(count > 1000000000):
                return -1
    return count

#                 1   2 2   3 3   4 4 4
print(MySolution2([0,1,0,1,1,0,1,1,0,1,1,1]))