string = input()

while True:
    if string.find('pi') >= 0:
        string = string.replace('pi', ' ')
        continue
    elif string.find('ka') >= 0:
        string = string.replace('ka', ' ')
        continue
    elif string.find('chu') >= 0:
        string = string.replace('chu', ' ')
        continue
    if len(string.strip()) == 0:
        print('YES')
        break
    else:
        print('NO')
        break