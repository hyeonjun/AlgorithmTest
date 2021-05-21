def solution(record):
    answer = []
    check = {}
    tmp = []
    for i in record:
        data = i.split(' ')
        if data[0] == "Enter":
            message = '님이 들어왔습니다.'
            check[data[1]] = data[2]
            tmp.append([data[1], message])
        elif data[0] == "Leave":
            message = '님이 나갔습니다.'
            tmp.append([data[1], message])
        else:  # Change
            check[data[1]] = data[2]
    for i in tmp:  # 아이디 -> 닉네임
        answer.append(check[i[0]] + i[1])
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))