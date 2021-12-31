book = {}
for _ in range(int(input())):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1
top = max(book.values())
answer = []
for i in book.keys():
    if book[i] == top:
        answer.append(i)
print(sorted(answer)[0])
