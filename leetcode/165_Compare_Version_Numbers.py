from itertools import zip_longest
# zip_longest: 길이가 다른 자료형을 길이가 긴 쪽에 맞춰서 zip 해주며,
# fillvalue를 사용하여 부족한 길이를 해당 값으로 채워줌
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = map(int, version1.split('.'))
        version2 = map(int, version2.split('.'))

        for x, y in zip_longest(version1, version2, fillvalue=0):
            if x > y:
                return 1
            if x < y:
                return -1
        return 0
