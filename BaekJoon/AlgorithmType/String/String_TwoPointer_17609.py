def pseudo_palindrome(S, left, right):
    while left < right:
        if S[left] == S[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def palindrome(S, left, right):
    while left < right:
        if S[left] == S[right]:
            left += 1
            right -= 1
        else: # 같지 않은 문제 삭제
            if pseudo_palindrome(S, left+1, right) or pseudo_palindrome(S, left, right-1):
                return 1
            else: # 삭제해도 다른게 있으면 두 개 이상을 삭제해야하므로 불가능
                return 2
    return 0

for _ in range(int(input())):
    string = input()
    left, right = 0, len(string)-1
    print(palindrome(string, left, right))