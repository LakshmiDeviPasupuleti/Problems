class Solution:
    def largestEven(self, s: str) -> str:
        if "2" not in s:
            return ""
        i=s.rfind("2")
        return s[:i+1]