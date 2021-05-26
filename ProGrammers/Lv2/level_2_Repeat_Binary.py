def solution(s):
    zero, count = 0 , 0
    while s != "1":
        zero += s.count("0")
        count += 1
        s = s.replace("0", "")
        s = str(bin(len(s)))[2:]
    return [count, zero]

print(solution("110010101001")) # [3,8]
print(solution("01110")) # [3,3]
print(solution("1111111")) # [4,1]