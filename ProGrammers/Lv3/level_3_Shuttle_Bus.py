def solution(n, t, m, timetable):
    crew = [int(tb[:2]) * 60 + int(tb[3:]) for tb in timetable]
    crew.sort()

    bus = [[540 + t * i, 0, None] for i in range(n)]

    bi, ci = 0, 0
    while ci < len(crew):
        c = crew[ci]
        if bi == len(bus):
            break
        if c <= bus[bi][0] and bus[bi][1] < m:
            bus[bi][1] += 1
            bus[bi][2] = c
            ci += 1
        else:
            bi += 1
    answer = bus[-1][0]
    if bus[-1][2] != None and bus[-1][1] == m:
        answer = bus[-1][2] - 1
    return '%02d:%02d' % (answer // 60, answer % 60)

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])) # "09:00"
print(solution(2,10,2,["09:10", "09:09", "08:00"])) # "09:09"
print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"])) # "08:59"
print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"])) # "00:00"
print(solution(1,1,1,["23:59"])) # "09:00"
# "18:00"
print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))