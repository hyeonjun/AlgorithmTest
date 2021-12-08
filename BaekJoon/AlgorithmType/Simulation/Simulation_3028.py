dic = {'A':(0,1), 'B':(1,2), 'C':(0,2)}
order = input()
cup = [1, 0, 0]
for o in order:
    x, y = dic[o]
    cup[x], cup[y] = cup[y], cup[x]
print(cup.index(1)+1)