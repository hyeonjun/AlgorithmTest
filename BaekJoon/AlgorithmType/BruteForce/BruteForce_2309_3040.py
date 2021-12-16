arr = [int(input()) for _ in range(9)]
sumV = sum(arr)
sub1, sub2 = 0, 0
for i in range(8):
    for j in range(i+1, 9):
        if sumV - (arr[i] + arr[j]) == 100:
            sub1, sub2 = arr[i], arr[j]
            break
arr.remove(sub1); arr.remove(sub2)
for i in arr:
    print(i)