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
            # print(right, left, i, sum(divmod(abs(i - right), 3)), sum(divmod(abs(i - left), 3)))
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
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))

def solution(numbers, hand):
    answer = ''
    keypad = [[3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    left = [3, 0]
    right = [3, 2]

    for i in numbers:
        if i in [1, 4, 7]:
            left = keypad[i]
            answer += 'L'
        elif i in [3, 6, 9]:
            right = keypad[i]
            answer += 'R'
        else:
            r_distance = abs(right[0] - keypad[i][0]) + abs(right[1] - keypad[i][1])
            l_distance = abs(left[0] - keypad[i][0]) + abs(left[1] - keypad[i][1])
            # print(right, left, i, r_distance, l_distance)
            if l_distance == r_distance:
                if hand == 'right':
                    right = keypad[i]
                    answer += 'R'
                else:
                    left = keypad[i]
                    answer += 'L'
            elif l_distance < r_distance:
                left = keypad[i]
                answer += 'L'
            else:
                right = keypad[i]
                answer += 'R'
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))

