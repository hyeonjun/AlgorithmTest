class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        a = [poured]
        for _ in range(query_row):
            b = [0 for _ in range(len(a)+1)]
            for i in range(len(a)):
                pour = (a[i] - 1) / 2
                if pour > 0:
                    b[i] += pour
                    b[i+1] += pour
            a = b
        return min(1, a[query_glass])
