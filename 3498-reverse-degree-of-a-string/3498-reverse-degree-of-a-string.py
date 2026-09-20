class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            rev_n=26-(ord(s[i])-ord('a'))
            pos=i+1
            total +=rev_n*pos
        return total