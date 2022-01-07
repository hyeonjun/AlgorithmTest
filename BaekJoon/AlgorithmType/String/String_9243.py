n = int(input())
a, b = list(map(int, input())), list(map(int, input()))
if n % 2:
    for i in range(len(a)):
        a[i] = 1-a[i]
print('Deletion succeeded' if a == b else 'Deletion failed')