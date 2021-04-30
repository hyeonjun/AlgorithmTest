def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = 0
    same_num_count = 0
    for i in lottos:
        if i == 0:
            zero_count += 1
        else:
            if i in win_nums:
                same_num_count += 1
        if zero_count == 6:
            return [1, 6]
    answer[0] = rank[same_num_count + zero_count]
    answer[1] = rank[same_num_count]

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))