# A C G T
# 1 2 3 4
def solution(S,P,Q):
    coefficient = {"A":"1","C":"2","G":"3","T":"4"}
    S_ = ""
    for i in S:
        S_+=(coefficient[i])

    checker = list(map(lambda p,q : [p,q], P,Q))
    check = "4"
    result = []
    for i in checker:
        for j in (S_[i[0]:i[1]+1]):
            if(check > j) : check=j
        result.append(int(check))
        check="4"
    return result

print(solution("CAGCCTA",[2,5,0],[4,5,6]))