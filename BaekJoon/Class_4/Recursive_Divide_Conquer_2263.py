import sys
sys.setrecursionlimit(1000000)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

location = {}
for i in range(n):
    location[in_order[i]] = i
result = []
def divide(in_start, in_end, post_start, post_end): # 중위순회 범위, 후위순회 범위
    if in_start > in_end or post_start > post_end:
        return

    parent = post_order[post_end] # 후위 순회에서 부모노드 찾기
    print(parent, end=" ") # 전위는 부모노드부터 출력
    result.append(parent)

    left = location[parent] - in_start # 왼쪽 인자 갯수
    right = in_end - location[parent] # 오른쪽 인자 갯수
    # print(left, right, location[parent])
    divide(in_start, in_start+left-1, post_start, post_start+left-1) # 왼쪽 노드
    divide(in_end-right+1, in_end, post_end-right, post_end-1) # 오른쪽 노드

divide(0, n-1, 0, n-1)
print(result)
"""
7
1 2 3 4 5 6 7
1 3 2 5 7 6 4
=> 4 2 1 3 6 5 7
"""

"""
후위 순회는 마지막 노드가 루트.
중위 순회는 루트를 기준으로 나눈다
후위 순회에서 부모 노드를 찾고, 중위 순회에서 기준으로 삼아 왼쪽, 오른쪽 나눔

idx   0    1    2    |3|    4    5     6
중위  (1   |2|   3)   |4|   (5   |6|    7)
후위  (1    3   |2|)  (5     7   |6|)  |4|
전위  |4| (|2|   1     3)  (|6|   5     7) 

1. divide(in_start, in_end, post_start, post_end) -> (0, 6, 0, 6)
parent = 4, parent_idx = 3
left = 3-0 = 3 => in_start(0), in_start(0)+left(3)-1 (중위, 0~2) , post_start(0), post_start(0)+left(3)-1 (후위, 0~2)
right = 6-3 = 3 => in_end(6)-right(3)+1, in_end (중위, 4~6) , post_end-right, post_end-1 (후위, 3~5)


2. divide(0,2,0,2) => 왼쪽
parent = 2, parent_idx = 1
left = 1(idx)-0(in_start) = 1 => 
 in_start, in_start+left-1 -> 0, 0+1-1= 0 (중위, 0~0) 
 post_start, post_start+left-1 -> 0, 0+1-1= 0 (후위, 0~0) => 3. divide(0,0,0,0)
right = 2(in_end)-1(idx) = 0
 in_end-right+1, in_end -> 2-1+1=2, 2(중위, 2~2)
 post_end-right, post_end-1 -> 1, 1 (후위, 1~1) => 4. divide(2,2,1,1)

5. divide(4,6,3,5) => 오른쪽
...
"""