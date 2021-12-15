string = input()
dic = [0 for _ in range(26)]
for s in string:
    dic[ord(s)-ord('A')] += 1

odd, cnt = '', 0
answer = ''
for i in range(26):
    if dic[i] % 2 == 1:
        cnt += 1
        odd += chr(i+ord('A'))
    answer += chr(i+ord('A')) * (dic[i] // 2)

if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer + odd + answer[::-1])