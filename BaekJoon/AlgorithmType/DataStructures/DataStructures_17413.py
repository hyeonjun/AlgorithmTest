string = input()
answer = ''
tmp = ''
tag = False
for s in string:
    if not tag:
        if s == '<':
            tag = True
            tmp += s
        elif s == ' ':
            answer += tmp+' '
            tmp = ''
        else:
            tmp = s + tmp
    else:
        tmp += s
        if s == '>':
            tag = False
            answer += tmp
            tmp = ''
print(answer+tmp)