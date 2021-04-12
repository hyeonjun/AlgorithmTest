##############################################################################
# Lesson 1 - BinaryGap
##############################################################################
def solution(N):
    binary = bin(N)[2:]
    ans = []
    next =""
    for i, value in enumerate(binary):
        if(value == '1'):
            temp = next
            next = i
            prev = temp
            if(prev != ""):
                if(next < prev):
                    ans.append(-(next-temp))
                else:
                    ans.append(next-prev)
    if(len(ans) == 0):
        return 0
    else:
        return max(ans)

N = 1041
print(solution(N))

def notation(N, base):
    T = "0123456789ABCDEF"
    quotient = N//base
    remainder = N%base
    # quotient, remainder = divmod(N, base)
    if quotient == 0:
        return T[remainder]
    else:
        return notation(quotient, base) + T[remainder]


print(notation(233, 2))
print(notation(233, 8))
print(notation(233, 16))

def binary(N):
    if(N == 0):
        return ""
    else:
        return binary(N//2)+str(N%2)
N =233
print(binary(N))