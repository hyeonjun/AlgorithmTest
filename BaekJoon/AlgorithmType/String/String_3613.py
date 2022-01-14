variance = input()
answer = ''
if '_' in variance:
    if variance[0] == '_' or variance[-1] == '_' or '__' in variance:
        answer = 'Error!'
    else:
        underbar = False
        for v in variance:
            if v.isupper():
                answer = 'Error!'
                break
            if v == '_':
                underbar = True
                continue
            if underbar:
                answer += v.upper()
                underbar = False
                continue
            answer += v
else:
    if variance[0].isupper():
        answer = 'Error!'
    else:
        for v in variance:
            if v.isupper():
                answer += '_'+v.lower()
            else:
                answer += v
print(answer)