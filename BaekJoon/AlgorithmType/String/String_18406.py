num = input()
if sum(list(map(int, num[:len(num)//2]))) == sum(list(map(int, num[len(num)//2:]))):
    print('LUCKY')
else:
    print('READY')