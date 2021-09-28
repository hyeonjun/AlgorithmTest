L = int(input())
string = input()
print(sum([(ord(string[i]) - ord('a')+1) * (31 ** i) for i in range(L)]) % 1234567891)