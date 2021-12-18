def palindrom(s):
    return True if s == s[::-1] else False

def notation(n, base):
    result = []
    while n > 0:
        q, r = divmod(n, base)
        n = q
        result.insert(0, r)
    return result

for _ in range(int(input())):
    n = int(input())
    flag = False
    for i in range(2, 65):
        if palindrom(notation(n, i)):
            flag = True
            break
    print(1 if flag else 0)