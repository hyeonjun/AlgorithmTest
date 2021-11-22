n = int(input())
arr = input()
L = arr.count('LL')
if L <= 1:
    print(len(arr))
else:
    arr = arr.replace('LL', 'S')
    print(len(arr)+1)

# ==================================
n = int(input())
arr = input()
L = arr.count('LL')
if L <= 1:
    print(len(arr))
else:
    print(len(arr)-L+1)