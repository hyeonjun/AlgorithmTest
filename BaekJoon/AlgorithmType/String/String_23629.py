num2str = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"}
str2num = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
operation = ['+', '-', 'x', '/', '=']
string = input()

for key, value in str2num.items():
    string = string.replace(key, str(value))
if string.isupper():
    print("Madness!")
    exit()

queue = []
num = 0
for i in range(len(string)):
    if string[i].isdigit():
        num *= 10 # 자리수 올리기
        num += int(string[i])
    else:
        if string[i-1] in operation:
            print("Madness!")
            exit()
        queue.append(num)
        num = 0
        queue.append(string[i])

n1 = queue[0]
for i in range(1, len(queue)-1, 2):
    op = queue[i]
    n2 = queue[i+1]
    if n2 in operation:
        print("Madness!")
        exit()
    if op == '+':
        n1 += n2
    elif op == '-':
        n1 -= n2
    elif op == 'x':
        n1 *= n2
    elif op == '/':
        if n1 < 0:
            n1 = -(abs(n1) // n2)
        else:
            n1 = n1 // n2
    else:
        print("Madness!")
        exit()

print(string)
if n1 < 0:
    print('-', end='')
for n in str(abs(n1)):
    print(num2str[int(n)], end='')