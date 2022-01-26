class Solution:
    def isValid(self, strs: str) -> bool:
        stack = []
        for s in strs:
            if s == '(' or s == '[' or s == '{':
                stack.append(s)
            elif s == ')' or s == '}' or s == ']':
                if not stack:
                    return False
                else:
                    d = stack.pop()
                    if s == ')' and d != '(':
                        return False
                    elif s == '}' and d != '{':
                        return False
                    elif s == ']' and d != '[':
                        return False

        return False if stack else True

class Solution:
    def isValid(self, strs: str) -> bool:
        stack = []
        dic = {')':'(', ']':'[', '}':'{'}
        for s in strs:
            if s in dic.values():
                stack.append(s)
            elif s in dic.keys():
                if len(stack) == 0 or stack.pop() != dic[s]:
                    return False
        return stack == []