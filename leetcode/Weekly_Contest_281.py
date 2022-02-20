# 1 - 6012. Count Integers With Even Digit Sum
class Solution:
    def countEven(self, num: int) -> int:
        answer = 0
        for i in range(2, num+1):
            if not sum(list(map(int, list(str(i))))) % 2:
                answer += 1
        return answer

# 2 - 6013. Merge Nodes in Between Zeros
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = dummy = ListNode(0)
        sumV = ListNode(0)
        while head.next:
            head = head.next
            if head.val == 0:
                dummy.next = sumV
                dummy = dummy.next
                sumV = ListNode(0)
            else:
                sumV.val += head.val
        answer = answer.next
        return answer

# 3 - 6014. Construct String With Repeat Limit
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        alpha = [0] * 26
        for i in s:
            alpha[ord(i) - ord('a')] += 1
        prev = -1
        answer = ''
        while True:
            visit, change = False, False
            for i in range(25, -1, -1):
                if i != prev and alpha[i] > 0:
                    change = True
                    if visit:
                        answer += chr(ord('a') + i)
                        alpha[i] -= 1
                    else:
                        cnt = min(alpha[i], repeatLimit)
                        answer += chr(ord('a') + i) * cnt
                        alpha[i] -= cnt
                    prev = i
                    break
                elif alpha[i] > 0:
                    visit = True
            if not change:
                break
        return answer

# 4 - 2183. Count Array Pairs Divisible by K
from collections import defaultdict
from math import gcd
class Solution:
    def coutPairs(self, nums: list[int], k: int) -> int:
        answer = 0
        dic = defaultdict(int)
        for n in nums:
            print(dic)
            answer += sum(dic[d] for d in dic if not d * n % k)
            dic[gcd(n, k)] += 1
            print(dic)
        return answer
