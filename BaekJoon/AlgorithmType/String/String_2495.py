for _ in range(3):
    A = input()
    answer = [1 for _ in range(8)]
    for i in range(8):
        count = 0
        for j in range(i+1, 8):
            if A[i] == A[j]:
                answer[i] += 1
            else:
                break
    print(max(answer))