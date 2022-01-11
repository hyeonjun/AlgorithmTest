import re
n = int(input())
word = list(map(int, re.findall(r'[0-9]+', input())))
print(sum(word))