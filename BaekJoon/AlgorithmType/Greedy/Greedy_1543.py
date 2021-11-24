string = input()
target = input()
answer = 0
start, end = 0, len(target)
while start <= len(string)-len(target):
    if string[start:end] == target:
        answer += 1
        start, end = end, end+len(target)
    else:
        start, end = start+1, end+1
print(answer)