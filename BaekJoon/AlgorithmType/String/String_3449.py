for _ in range(int(input())):
    A = input()
    B = input()
    answer = 0
    for a, b in zip(A, B):
        if a != b:
            answer += 1
    print(f'Hamming distance is {answer}.')