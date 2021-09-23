n = int(input())
cnt, num = 1, 666
while cnt < n:
    num += 1
    if '666' in str(num):
        cnt += 1
print(num)

"""
2
=> 1666

8
=> 6661
"""