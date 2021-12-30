for i in range(int(input())):
    string = list(input().split())[::-1]
    print(f'Case #{i+1}:', *string)

# 스택
for i in range(int(input())):
    string = list(input().split())
    print(f'Case #{i+1}:', end=" ")
    while string:
        print(string.pop(), end=" ")
    print()