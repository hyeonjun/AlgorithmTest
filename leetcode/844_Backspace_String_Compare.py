# Solution1 - Stack, 32ms
class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for i in string:
                if i == '#':
                    if stack:
                        stack.pop()
                    continue
                stack.append(i)
            return stack
        return build(s) == build(t)


# Solution2 - Two Pointer, 53 ms
class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        n, m = len(S) - 1, len(T) - 1

        def get(string, idx):
            count = 0  # '#' count
            while idx >= 0:
                if string[idx] == '#':
                    count += 1
                elif count:
                    count -= 1
                else:
                    break
                idx -= 1
            return idx

        while n >= 0 or m >= 0:
            if n >= 0:
                n = get(S, n)
            if m >= 0:
                m = get(T, m)
            if n >= 0 and m >= 0 and S[n] != T[m]:
                return False
            if (n >= 0) != (m >= 0):
                return False
            n -= 1
            m -= 1
        return True

solution = Solution2()
print(solution.backspaceCompare("y#fo##f", "y#f#o##f"))