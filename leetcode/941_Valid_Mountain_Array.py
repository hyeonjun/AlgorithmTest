class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        idx = 0
        for i in range(1, len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if arr[i] > arr[i+1]:
                idx = i
                break
        for i in range(idx, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True