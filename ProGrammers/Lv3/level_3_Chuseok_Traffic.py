def solution(lines):
    def time_split(data):
        date, time, runtime = data.split()
        h, m, s = time.split(':')
        # 소수점이 있어서 시간을 전부 밀리초로 변경
        time = int((int(h) * 3600 + int(m) * 60 + float(s)) * 1000)
        runtime = int(float(runtime[:-1]) * 1000)
        # 01:00:02.003 ~ 01:00:04.002 = time-runtime+1
        return [time - runtime + 1, time]  # [시작시간, 종료시간]

    time_data = list(map(time_split, lines))
    answer = 0

    def checker(start, time):
        count = 0
        end = start + 1000  # 1 초
        for t in time:
            if t[0] < end and start <= t[1]:
                count += 1
        return count

    for t in time_data:
        answer = max(answer, checker(t[0], time_data), checker(t[1], time_data))

    return answer

# 1
print(solution(["2016-09-15 00:00:00.000 3s"]))
# 1
print(solution(["2016-09-15 23:59:59.999 0.001s"]))
# 1
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
# 2
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
# 7
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
# 1
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))