def solution(a, b):
    answer = ''
    # 1
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = day[(sum(month[:a - 1]) + b) % 7]
    # 2
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    from datetime import datetime
    answer = day[datetime(2016, a, b).weekday()]

    return answer

print(solution(5,24))