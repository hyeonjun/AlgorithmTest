# 168 - Excel Sheet Column Title
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ''
        while columnNumber > 0:
            answer += chr((columnNumber-1) % 26 + ord('A'))
            columnNumber = (columnNumber - 1) // 26
        return answer[::-1]

# 171 - Excel Sheet Column Number
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        columnTitle = columnTitle[::-1]
        for i in range(len(columnTitle)):
            answer += (26 ** i) * (ord(columnTitle[i]) - ord('A') + 1)
        return answer
