def solution(dirs):
    move = {"U":[0,1], "D":[0,-1], "R":[1,0], "L":[-1,0]}
    street = set()
    start = [0,0]

    for i in dirs:
        tmpX = start[0] + move[i][0]
        tmpY = start[1] + move[i][1]
        if -5 <= tmpX <= 5 and -5 <= tmpY <= 5:
            street.add((start[0], start[1], tmpX, tmpY))
            street.add((tmpX, tmpY, start[0], start[1]))
            start = [tmpX, tmpY]
    return len(street) // 2

print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7
print(solution("LRLRL")) # 1