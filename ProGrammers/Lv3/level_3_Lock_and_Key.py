def solution(key, lock):
    lock_s = len(key) - 1
    lock_e = lock_s + len(lock)
    padding = (len(key) - 1) * 2 + len(lock)

    def rotation(key):
        return list(zip(*key[::-1]))

#     def rotation(arr):
#         n = len(arr)
#         ret = [[0] * n for _ in range(n)]

#         for i in range(n):
#             for j in range(n):
#                 ret[j][n-1-i] = arr[i][j]
#         return ret

    def check(x, y, key, lock, padding, lock_s, lock_e):
        paddingList = [[0] * padding for _ in range(padding)]

        for i in range(len(key)):  # key 추가
            for j in range(len(key)):
                paddingList[x + i][y + j] += key[i][j]

        for i in range(lock_s, lock_e):
            for j in range(lock_s, lock_e):
                paddingList[i][j] += lock[i - lock_s][j - lock_s]
                if paddingList[i][j] != 1:
                    return False
        return True

    for rotate in range(4):
        for i in range(lock_e):
            for j in range(lock_e):
                if check(i, j, key, lock, padding, lock_s, lock_e):
                    return True
        key = rotation(key)
    return False
# True
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
