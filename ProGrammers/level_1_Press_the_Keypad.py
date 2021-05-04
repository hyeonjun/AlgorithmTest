def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for i in numbers:
        if i in [1, 4, 7]:
            left = i
            answer += 'L'
        elif i in [3, 6, 9]:
            right = i
            answer += 'R'
        else:
            i = 11 if i == 0 else i
            print(right, left, i, sum(divmod(abs(i - right), 3)), sum(divmod(abs(i - left), 3)))
            if sum(divmod(abs(i - right), 3)) > sum(divmod(abs(i - left), 3)):
                left = i
                answer += 'L'
            elif sum(divmod(abs(i - right), 3)) < sum(divmod(abs(i - left), 3)):
                right = i
                answer += 'R'
            else:
                if hand == 'right':
                    right = i
                    answer += 'R'
                else:
                    left = i
                    answer += 'L'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
