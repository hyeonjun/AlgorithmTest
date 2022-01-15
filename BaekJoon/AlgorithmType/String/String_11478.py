S = input()
answer = set()
for i in range(1, len(S)+1): # 길이
    for j in range(len(S)-i+1): # 스타트
        answer.add(S[j:j+i])

print(len(answer))