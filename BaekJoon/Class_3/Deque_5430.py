for i in range(int(input())):
    p = input().replace('RR', '')
    n = int(input())
    arr = input()[1:-1].split(",")

    # 명령에 따라 배열을 뒤집거나 원소 삭제를 해서는 안된다.
    # 뒤집거나 삭제를 실제로 하지 않고 그와 같은 효과를 내도록 구현해야 시간 초과를 벗어낳 수 있다.
    is_reverse = False
    flag = True
    start, end = 0, 0

    for c in p:
        if c == 'R':
            is_reverse = not is_reverse
        else:
            if is_reverse:
                end += 1
            else:
                start += 1

    if start + end <= n:
        result = arr[start:n-end]
        if is_reverse:
            print("[" + ",".join(result[::-1]) + "]")
        else:
            print("[" + ",".join(result) + "]")
    else:
        print("error")