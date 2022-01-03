while True:
    string = input()
    if string == '#':
        break
    dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for s in string.lower():
        if s in dic:
            dic[s] += 1
    print(sum(dic.values()))