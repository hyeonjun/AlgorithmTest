caesar = input()
for c in caesar:
    print(chr((ord(c)-ord('A')-3) % 26 + ord('A')), end='')