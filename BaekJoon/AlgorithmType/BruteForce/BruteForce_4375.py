while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    count = 0
    while True:
        num += 10 ** count
        count += 1
        if num % n == 0:
            print(count)
            break