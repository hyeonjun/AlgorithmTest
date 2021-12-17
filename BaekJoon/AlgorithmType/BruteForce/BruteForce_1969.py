n, m = map(int, input().split())
dna = [list(input()) for _ in range(n)]
dna_num = {'A':0, 'C':1, 'G':2, 'T':3}
num_dna = {0:'A', 1:'C', 2:'G', 3:'T'}
hamming = []
distance = 0
for i in zip(*dna):
    cnt = [0, 0, 0, 0]
    for j in i:
        cnt[dna_num[j]] += 1
    maxIdx = cnt.index(max(cnt))
    hamming.append(num_dna[maxIdx])
    cnt[maxIdx] = 0
    distance += sum(cnt)
print(''.join(hamming))
print(distance)