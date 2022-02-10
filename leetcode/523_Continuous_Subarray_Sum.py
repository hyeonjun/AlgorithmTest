"""
if sum(nums[i:j]) % k == 0 일 때
 i < j 이라면,
 sum(nums[:j]) % k == sum(nums[:i]) % k
 j - i > 1, return True
"""
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        dic = {0: 0} # modulo value : index
        S = 0
        for i, v in enumerate(nums, 1):
            S = (S + v) % k
            if S not in dic:
                dic[S] = i
            elif i-dic[S] > 1:
                return True
        return False