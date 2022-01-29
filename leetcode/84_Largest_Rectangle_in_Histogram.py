class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = []
        answer = 0
        heights = heights + [0] # 마지막 막대도 계산하기 위해
        for i in range(n+1):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()] # 먼저 pop 하지 않으면 stack에 있는 값에 의해 제대로된 w를 구할 수 없다.
                w = i-stack[-1]-1 if stack else i # 위에서 먼저 pop 했기 때문에 -1 해줘야한다
                answer = max(answer, h*w)
            stack.append(i)
        return answer