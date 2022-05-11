arr = [''] + list(input())
answer = 0
for i in range(1, len(arr)):
    if arr[i] == 'Y':
        answer += 1
        for j in range(i, len(arr), i):
            arr[j] = 'N' if arr[j] == 'Y' else 'Y'
print(answer)