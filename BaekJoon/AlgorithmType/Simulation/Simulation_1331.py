direction = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]
answer = "Valid"
arr = [input() for _ in range(36)]
if len(set(arr)) != 36:
    print('Invalid')
else:
    for i in range(35):
        if abs( ord(arr[i][0]) - ord(arr[i+1][0]) ) * abs( int(arr[i][1]) - int(arr[i+1][1]) ) != 2:
            answer = "Invalid"
            break
    else:
        for x, y in direction:
            a, b = ord(arr[-1][0]) + x, int(arr[-1][1]) + y
            if ord('A') <= a <= ord('F') and 1 <= b <= 6:
                if arr[0][0] == chr(a) and b == int(arr[0][1]):
                    answer = "Valid"
                    break
        else:
            answer = "Invalid"
    print(answer)