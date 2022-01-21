"""
trie : 여러 개의 문자열 집합에서 원하는 문자열을 찾는다.
KMP : 매우 긴 문자열에서 원하는 문자열을 찾는다.
"""
def getPi():
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

def KMP():
    getPi()
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = pi[j-1]
        if string[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False

string = input()
pattern = input()
pi = [0 for _ in range(len(pattern))]
print(int(KMP()))