for _ in range(int(input())):
    arr = [list(input().split()) for _ in range(int(input()))]
    arr.sort(key=lambda x:(int(x[0])), reverse=True)
    print(arr[0][1])