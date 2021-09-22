# 1152
string = list(map(str, input().split()))
print(len(string))

# 1157
string = list(input().upper())
dic = []
for i in set(string):
    dic.append(string.count(i))
idx = [i for i, v in enumerate(dic) if max(dic) == v]
print('?') if len(idx) > 1 else print(list(set(string))[idx[-1]])
