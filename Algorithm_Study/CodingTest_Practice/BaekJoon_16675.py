# 두 개의 손
def solution(srp):
    ml, mr, tl, tr = ('SRP'.index(i) for i in srp)
    if ml == mr and (ml+1) % 3 in [tl, tr]:
        return 'TK'
    elif tl == tr and (tl+1) % 3 in [ml, mr]:
        return 'MS'
    else:
        return '?'
# 0 <- 1 <- 2 <- 0
print(solution(['R','S','P','R'])) # ?
print(solution(['R','R','S','S'])) # MS
print(solution(['P','P','S','R'])) # TK