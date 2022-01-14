num = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
n, m = map(int, input().split())
answer = []
for i in range(n, m+1):
    tmp = ' '.join([num[x] for x in str(i)])
    answer.append([i, tmp])
answer.sort(key=lambda x:x[1])
for i in range(len(answer)):
    if i % 10 == 0 and i !=0:
        print()
    print(answer[i][0], end=' ')