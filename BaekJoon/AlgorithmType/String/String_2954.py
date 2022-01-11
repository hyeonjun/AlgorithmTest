string = list(input())
answer = ''
while string:
    x = string.pop(0)
    if x in ('a','e','i','o','u') and string:
        string.pop(0)
        string.pop(0)
    answer += x
print(answer)