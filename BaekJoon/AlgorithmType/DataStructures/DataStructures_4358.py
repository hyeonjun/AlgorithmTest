import sys
input = sys.stdin.readline
tree = {}
total = 0
while True:
    name = input().strip()
    if not name:
        break
    total += 1
    if name in tree:
        tree[name] += 1
    else:
        tree[name] = 1
for k in sorted(tree.keys()):
    print("{0} {1:.4f}".format(k, tree[k]/total*100))