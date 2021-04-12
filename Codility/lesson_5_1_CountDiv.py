# def MySolution(A,B,K): # 50%
#     count = 0
#     for i in range(A,B+1):
#         if(i % K == 0):
#             count += 1
#     return count
# print(MySolution(0,0,11))

def MySolution2(A,B,K): # 100%
    count=(B//K)-(A//K)
    if(A%K==0):count+=1
    return count

print(MySolution2(11,14,2))
