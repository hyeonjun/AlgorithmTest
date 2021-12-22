n = int(input())
left, right = input().split('*')
for _ in range(n):
    string = input()
    if left == string[:len(left)] and right == string[-len(right):] and len(''.join(left+right)) <= len(string):
        print('DA')
    else:
        print('NE')