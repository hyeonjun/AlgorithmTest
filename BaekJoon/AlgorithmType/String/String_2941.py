croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()
for c in croatia:
    string = string.replace(c, '*')
print(len(string))