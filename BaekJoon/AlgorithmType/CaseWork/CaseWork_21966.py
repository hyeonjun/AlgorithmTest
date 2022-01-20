n = int(input())
string = input()
if n <= 25:
    print(string)
else:
    mid = string[11:n-11]
    idx = mid.find('.')
    if idx == -1 or len(mid)-1 == idx:
        print(string[:11]+'...'+string[n-11:])
    else:
        print(string[:9]+'......'+string[n-10:])