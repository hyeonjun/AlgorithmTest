string = input()
answer = [string[i:] for i in range(len(string))]
answer.sort()
for a in answer:
    print(a)
