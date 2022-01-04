for _ in range(int(input())):
    n, string = input().split()
    print(string[:int(n)-1]+string[int(n):])