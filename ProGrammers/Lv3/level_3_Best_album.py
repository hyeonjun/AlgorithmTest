def solution(genres, plays):
    answer = []
    from collections import defaultdict
    gp_dict = defaultdict(int)
    for g, p in zip(genres, plays):
        gp_dict[g] += p
    gp_dict = sorted(gp_dict, reverse=True, key=lambda x: gp_dict[x])

    while len(gp_dict) > 0:
        data = gp_dict.pop(0)
        a, b = 0, 0
        for i, v in enumerate(genres):
            if v == data:
                if plays[i] >= a:
                    a, b = plays[i], a
                elif b < plays[i] < a:
                    b = plays[i]
        a = plays.index(a)
        answer.append(a)
        plays[a] = 0
        if b != 0:
            answer.append(plays.index(b))
    return answer

# [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# [4, 5, 1, 3]
print(solution(["classic", "pop", "classic", "pop", "classic", "classic"], [400, 600, 150, 600, 500, 500]))

def solution(genres, plays):
    from collections import defaultdict
    answer = []
    genre_dict = defaultdict(int)
    total_num = defaultdict(list)

    for i, v in enumerate(genres):
        genre_dict[v] += plays[i]
        total_num[v].append((plays[i], i))

    genre_dict = sorted(genre_dict, reverse=True, key=lambda x: genre_dict[x])

    for t in total_num:
        total_num[t] = sorted(total_num[t], key=lambda x: x[0], reverse=True)[:2]

    while len(genre_dict) > 0:
        genre = genre_dict.pop(0)
        print(genre)
        for t in total_num:
            if t == genre:
                if len(total_num[t]) > 1:
                    answer.extend([total_num[t][0][1], total_num[t][1][1]])
                else:
                    answer.append(total_num[t][0][1])

    return answer

# [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# [4, 5, 1, 3]
print(solution(["classic", "pop", "classic", "pop", "classic", "classic"], [400, 600, 150, 600, 500, 500]))
