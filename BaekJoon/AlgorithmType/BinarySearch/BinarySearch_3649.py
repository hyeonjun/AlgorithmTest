import sys
input = sys.stdin.readline
while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        arr = sorted(int(input()) for _ in range(n))

        left, right = 0, n-1
        while left < right:
            size = arr[left] + arr[right]
            if size == x:
                print('yes', arr[left], arr[right])
                break
            elif size < x:
                left += 1
            else:
                right -= 1
        else:
            print('danger')
    except:
        break