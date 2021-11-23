string = input()
cnt = 1
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        cnt += 1
print(cnt // 2)