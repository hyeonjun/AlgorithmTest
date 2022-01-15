import re
for _ in range(int(input())):
    string = input()
    # fullmatch : 패턴과 문자열이 남는 부분없이 완벽하게 일치하는지 검사
    if re.fullmatch(r'(100+1+|01)+', string):
        print('YES')
    else:
        print('NO')