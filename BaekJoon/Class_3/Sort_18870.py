n = int(input())
lst = list(map(int, input().split()))
lst_ = sorted(set(lst))
dic = {lst_[i] : i for i in range(len(lst_))}
for i in lst:
    print(dic[i], end=' ')