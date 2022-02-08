class Solution:
    def minimumSum(self, num: int) -> int:
        # 정렬 후 큰 수는 1의 자리로, 작은 수는 10의 자리로 만들어서 더하면 작은 수를 만들 수 있다.
        num = sorted(str(num))
        return int(num[0]) * 10 + int(num[1]) * 10 + int(num[2]) + int(num[3])