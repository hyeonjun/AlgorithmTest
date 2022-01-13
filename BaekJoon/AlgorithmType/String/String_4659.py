while True:
    string = input()
    if string == 'end':
        break
    v = ['a', 'e', 'i', 'o', 'u']
    v_cnt = 0
    v_repeat, c_repeat = 0, 0
    flag = True
    word = ''
    for s in string:
        if s in v:
            v_cnt += 1
            v_repeat += 1
            c_repeat = 0
            if v_repeat > 2:
                flag = False
                break
            if s == word:
                if s == 'e' or s == 'o':
                    pass
                else:
                    flag = False
                    break
        else:
            v_repeat = 0
            c_repeat += 1
            if c_repeat > 2:
                flag = False
                break
            if s == word:
                flag = False
                break
        word = s
    if v_cnt < 1:
        flag = False

    if flag:
        print(f'<{string}> is acceptable.')
    else:
        print(f'<{string}> is not acceptable.')