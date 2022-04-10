class Solution:
    def calPoints(self, ops: list[str]) -> int:
        arr = []
        for o in ops:
            if o[0] == '-' or o.isdigit():
                arr.append(int(o))
            elif o == '+':
                arr.append(arr[-1]+arr[-2])
            elif o == 'D':
                arr.append(arr[-1]*2)
            elif o == 'C':
                arr.pop()
            print(arr)
        return sum(arr)