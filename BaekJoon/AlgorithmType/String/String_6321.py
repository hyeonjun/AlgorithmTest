for i in range(1, int(input())+1):
    string = input()
    answer = ''
    for s in string:
        answer += chr( (ord(s)-ord('A')+1) % 26 + ord('A') )
    print(f'String #{i}')
    print(answer)
    print()