import sys
sys.setrecursionlimit(1000000)
pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break
def post_order(start, end):
    if start > end:
        return

    parent = pre_order[start] # 전위 => 루트 왼쪽 오른쪽

    # / 루트 /_____ 왼쪽 _____/(루트보다 처음 수가 커지는 부분)_____ 오른쪽 _____/
    right_start = end+1
    right_end = end
    for i in range(1, end-start+1):
        if parent < pre_order[start+i]:
            right_start = start+i
            break
    left_start = start + 1
    left_end = right_start - 1

    # 왼쪽
    post_order(left_start, left_end)
    # 오른쪽
    post_order(right_start, right_end)
    print(parent) # 후위는 부모를 나중에 출력

post_order(0, len(pre_order)-1)