"""
* 파이썬 NOT
    - 비트 반전 후, 2의 보수로 만들어서 리턴
      비트 반전 -> 1의 보수 -> 2의 보수 -> 음수 부호 붙여서 리턴

* 1의 보수 얻기
 mask = 원본 이진수의 자릿수만큼 1로 채운 것
 - ~A & mask
 - A ^ mask
 - mask - A
"""
a = int(input(), 2) # 2진수를 10진수로 받음
b = int(input(), 2)
mask = 2 ** 100000 - 1
print(bin(a&b)[2:].zfill(100000)) # zfill(X) : 문자열의 길이가 X보다 작을경우 부족한 길이만큼 0 채움
print(bin(a|b)[2:].zfill(100000))
print(bin(a^b)[2:].zfill(100000))
print(bin(mask-a)[2:].zfill(100000))
print(bin(mask-b)[2:].zfill(100000))