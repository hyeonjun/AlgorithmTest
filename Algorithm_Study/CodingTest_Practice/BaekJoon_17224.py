# APC는 왜 서브태스크 대회가 되었을까?
# 문제수, 역량, 풀수있는최대개수, 문제[쉬운문제나이도, 어려운문제난이도]
def solution(n, l, k, problem):
    easy, hard = 0, 0
    for i, j in problem:
        if j <= l:
            hard += 1
        elif i <= l:
            easy += 1
    hard = hard if hard < k else k
    easy = easy if easy < k-hard else k-hard
    return hard * 140 + easy * 100

print(solution(4, 8, 4, [[1,8],[4,5],[6,20],[9,12]])) # 380
print(solution(8,7,5, [[1,3],[2,5],[3,5],[4,8],[5,8],[6,9],[6,7],[7,10]])) # 660
print(solution(8,9,5,[[1,8],[3,10],[4,5],[5,20],[7,12],[8,15],[9,50],[14,14]])) # 580