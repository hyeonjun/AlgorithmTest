def solution(play_time, adv_time, logs):
    def str_to_int(time):
        h, m, s = time.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    def int_to_str(time):
        h = time // 3600
        h = '0' + str(h) if h < 10 else str(h)
        time = time % 3600
        m = time // 60
        m = '0' + str(m) if m < 10 else str(m)
        time = time % 60
        s = '0' + str(time) if time < 10 else str(time)
        return h + ':' + m + ':' + s

    # 모든 시간 초단위로 변경
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)

    # Memoization
    all_time = [0 for _ in range(play_time + 1)]

    # logs 내의 모든 시간 초로 환산 및 start, end 구분
    # all_time[i] = i 시각에 시청중인 사람의 수수
    for l in logs:
        start, end = l.split('-')
        start, end = str_to_int(start), str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    # 구간별 시청자 수 기록
    for i in range(1, len(all_time)):
        all_time[i] += all_time[i - 1] # (i-1부터 i까지) 1초 동안의 시청자 수

    # 모든 구간 시청자 누적 기록
    for i in range(1, len(all_time)):
        all_time[i] += all_time[i - 1]

    # 누적된 시청자수를 바탕으로 가장 시청자수가 많은 구간 탐색
    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                # 처음부터 끝까지 반복문을 탐색하면서
                # 구간대비 시청자 수가 가장 많은 곳을 찾는다.
                # 현재 i의 누적 시청자수에서 i-adv_time의 누적 시청자수를 빼면
                # 해당 구간의 시청자수 값을 얻는다
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)

# "01:30:59"
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# "01:00:00"
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# "00:00:00"
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))