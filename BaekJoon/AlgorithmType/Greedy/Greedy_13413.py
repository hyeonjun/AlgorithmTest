for _ in range(int(input())):
    n = int(input())
    current = input()
    target = input()

    black, white = [current.count('B'), target.count('B')], [current.count('W'), target.count('W')]
    diff = 0
    for i in range(n):
        if current[i] != target[i]:
            diff += 1

    # W,B 개수가 같으면 서로 위치만 변경
    if black[0] == black[1]:
        print(diff//2)
    # W,B 개수가 다르면 하나를 뒤집어서 갯수 맞추고 위치 변경
    else:
        reverse = abs(black[0] - black[1])
        print(reverse + (diff - reverse)//2)