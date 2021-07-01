# 걸그룹 마스터 준석이
def solution(team, test):
    for i in team:
        team[i].sort()

    answer = []
    for name, type in test:
        if type == 1:
            for j in team:
                if name in team[j]:
                    answer.append(j)
        else:
            for j in team[name]:
                answer.append(j)
    return '\n'.join(answer)


    pass

team = {
    'twice':[
        'jihyo',
        'dahyeon',
        'mina',
        'momo',
        'chaeyoung',
        'jeongyeon',
        'tzuyu',
        'sana',
        'nayeon'
    ],
    'blackpink':[
        'jisu',
        'lisa',
        'rose',
        'jenny'
    ],
    'redvelvet':[
        'wendy',
        'irene',
        'seulgi',
        'yeri',
        'joy',
    ]
}

test = [['sana', 1], ['wendy',1], ['twice', 0], ['rose', 1]]

print(solution(team, test))