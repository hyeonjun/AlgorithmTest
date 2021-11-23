string = input()
ucpc = ['U', 'C', 'P', 'C']
check = 0
for u in ucpc:
    if u in string:
        check += 1
        string = string[string.index(u)+1:]
    else:
        print('I hate UCPC')
        break
if check == 4:
    print('I love UCPC')