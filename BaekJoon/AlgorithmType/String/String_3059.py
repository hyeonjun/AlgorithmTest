for _ in range(int(input())):
    string = input()
    answer = 0
    for i in range(65, 91):
        if chr(i) not in string:
            answer += i
    print(answer)