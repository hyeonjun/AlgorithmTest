while True:
    number = sorted(list(map(int, input().split())))
    if number[0] == -1:
        break
    answer = 0
    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            if 2 * number[i] == number[j]:
                answer += 1
    print(answer)