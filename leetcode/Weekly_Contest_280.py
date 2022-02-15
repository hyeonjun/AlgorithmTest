# 1 - 2169. Count Operations to Obtain Zero
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == num2 == 0:
            return 0
        answer = 0
        while True:
            if num1 == 0 or num2 == 0:
                break
            if num1 < num2:
                num2 -= num1
            else:
                num1 -= num2
            answer += 1

        return answer

# 2 - 2170. Minimum Operations to Make the Array Alternating
# 이해가 잘 안된다.
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        x, y = defaultdict(int), defaultdict(int)
        n = len(nums)
        for i in range(n):
            if i % 2:
                x[nums[i]] += 1
            else:
                y[nums[i]] += 1
        x[-1], y[-2] = 0, 0 # tmp
        x = sorted(x.items(), key=lambda x:x[1], reverse=True)
        y = sorted(y.items(), key=lambda x:x[1], reverse=True)
        if x[0][0] != y[0][0]:
            return n - x[0][1] - y[0][1]
        return n - max(x[0][1]+y[1][1], x[1][1]+y[0][1])

# 3 - 2171. Removing Minimum Number of Magic Beans
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort() # [1, 4, 5 ,6]
        answer = 0
        for i in range(len(beans)):
            # i번 이전까지는 전부 0으로 생각하고 나머지는 해당 수로 만들었을 때의 합
            # 즉, 이중 최대값을 구해야 최소로 깍아야할 수가 나온다
            answer = max(answer, beans[i] * (len(beans) - i))
        return sum(beans) - answer

# 4 - 2172. Maximum AND Sum of Array
class Solution:
    def maximumANDSum(self, nums: List[int], m: int) -> int:
        n = len(nums)

        # @cache 데코레이터를 어떤 함수 위에 선언하면,
        # 그 함수에 넘어온 인자를 키(key)로 그리고 함수의 호출 결과를 값(value)으로 메모이제이션 적용.
        @cache
        def dfs(i, slot):
            if i == n:
                return 0
            res = 0
            slot = list(slot)
            for j in range(1, m+1):
                if slot[j] < 2:
                    slot[j] += 1 # 슬롯 하나 채움
                    res = max(res, (j & nums[i]) + dfs(i + 1, tuple(slot[:])))
                    slot[j] -= 1
            return res

        return dfs(0, tuple([0 for _ in range(m+1)]))
