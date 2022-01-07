for _ in range(int(input())):
    string = input()
    n = len(string)
    flag = False
    for i in range(n//2):
        if string[i] == string[n-i-1]:
            flag = True
        else:
            flag = False
    print('Do-it' if flag else 'Do-it-Not')