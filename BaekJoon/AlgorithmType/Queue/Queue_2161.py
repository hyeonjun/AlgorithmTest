num = [i for i in range(1, int(input())+1)]
while len(num) > 1:
    print(num.pop(0), end=" ")
    num.append(num.pop(0))
print(num[-1])
