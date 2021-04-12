def solution(H): # 개어렵네
    if len(H) == 1:
        return 1

    count = 1
    stack = [H[0]]
    for i in H:
        if i > stack[-1]:
            stack.append((i))
            count+=1
        elif i < stack[-1]:
            last = stack.pop()
            while i < last:
                if len(stack) == 0 :
                    break
                last = stack.pop()
            count+= 1
            if i > last:
                stack.append(last)
            elif i == last:
                count -= 1
            stack.append(i)
    return count

print(solution([8,8,5,7,9,8,7,4,8]))