class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            rev_value=26-(ord(s[i])-ord(('a')))
            pos=i+1
            total += rev_value * pos
        return total
        