for _ in range(int(input())):
    print("Distances: ", end='')
    A, B = input().split()
    for a, b, in zip(A, B):
        a, b = ord(a), ord(b)
        print(b-a if b >= a else b+26-a, end=" ")
    print()