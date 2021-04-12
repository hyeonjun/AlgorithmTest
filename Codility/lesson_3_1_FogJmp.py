def solution(X, Y, D):
    count = (Y-X)//D
    if(count*D < (Y-X)):
        count+= 1
    return count

# 현재위치, 도달위치, 이동할수있는거리
print((solution(5, 105, 3)))

