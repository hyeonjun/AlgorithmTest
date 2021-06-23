def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    graph = dict(zip(enroll, range(len(enroll))))

    for s, p in zip(seller, amount):
        p = p * 100
        while True:
            node = graph[s]  # 해당 사람의 번호
            profit = p // 10
            answer[node] += p - profit
            p = profit
            s = referral[node]
            if s == '-':
                break
            if profit == 0:
                break

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referrel = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referrel, seller, amount)) # [360, 958, 108, 0, 450, 18, 180, 1080]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]

print(solution(enroll, referral, seller, amount)) # [0, 110, 378, 180, 270, 450, 0, 0]