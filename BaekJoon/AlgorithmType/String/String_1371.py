import sys
string = sys.stdin.read()
word = [0 for _ in range(26)]
for s in string:
    if s.isalpha():
        word[ord(s) - ord('a')] += 1
maxV = max(word)
for i in range(26):
    if word[i] == maxV:
        print(chr(i+ord('a')), end='')