n = int(input())
tree = [list(map(int, input())) for _ in range(n)]

def quard(x, y, n):
    if n == 1:
        return str(tree[x][y])

    result = []
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tree[x][y] != tree[i][j]:
                result.append("(")

                result.extend(quard(x, y, n//2))
                result.extend(quard(x, y+n//2, n//2))
                result.extend(quard(x+n//2, y, n//2))
                result.extend(quard(x+n//2, y+n//2, n//2))

                result.append(")")
                return result
    return str(tree[x][y]) # 이 부분에는 모두 같은 값이므로 xy좌표의 값만 보내면 된다.

print("".join(quard(0,0,n)))

