def solution(string):
    idx = 0
    password = []
    for i in string:
        if i == '<':
            if idx != 0:
                idx -= 1
        elif i == '>':
            if idx < len(password):
                idx += 1
        elif i == '-':
            if len(password) > 0:
                del password[idx-1]
                idx -= 1
        else:
            password.insert(idx, i)
            idx += 1
    return ''.join(password)

print(solution("<<BP<A>>Cd-")) # BAPC
print(solution("ThIsIsS3Cr3t")) # ThIsIsS3Cr3t

def solution(string):
    left = []
    right = []
    for i in string:
        if i == '<':
            if len(left) > 0:
                right.append(left.pop())
        elif i == '>':
            if len(right) > 0:
                left.append(right.pop())
        elif i == '-':
            if len(left) > 0:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    return ''.join(left)



print(solution("<<BP<A>>Cd-")) # BAPC
print(solution("ThIsIsS3Cr3t")) # ThIsIsS3Cr3t