n, k = map(int, input().split())
nameLength = [0 for _ in range(n)] # 등수별 이름 길이 저장
student = [0 for _ in range(21)] # 이름 길이별 학생 수 저장
answer = 0

for i in range(n):
    name = len(input())
    nameLength[i] = name
    if i > k: # 학생 등수가 k보다 커지면 k범위 넘어가는 등수의 학생을 제거
        student[nameLength[i-k-1]] -= 1
    answer += student[name] # 자신의 이름과 길이가 같은 학생들로 쌍
    student[name] += 1 # 자신 추가
print(answer)