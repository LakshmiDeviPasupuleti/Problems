class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        maximum = 0
        res = ""

        if sum > num * 9:
            return ""

        for i in range(num):
            digit = min(9, sum)
            res += str(digit)
            sum -= digit

        return res