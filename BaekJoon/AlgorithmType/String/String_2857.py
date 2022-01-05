answer = []
for i in range(1, 6):
    if 'FBI' in input():
        answer.append(str(i))
if answer:
    print(*answer)
else:
    print('HE GOT AWAY!')