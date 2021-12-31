answer = set([])
for _ in range(int(input())):
    name, cmd = input().split()
    if cmd == 'enter':
        answer.add(name)
    else:
        answer -= {name}
for i in sorted(answer, reverse=True):
    print(i)