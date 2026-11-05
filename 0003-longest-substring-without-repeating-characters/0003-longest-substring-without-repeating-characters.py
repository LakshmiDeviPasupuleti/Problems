class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charmap={}
        left=0
        max_len=0
        for right in range(len(s)):
            ch=s[right]
            if ch in charmap:
                left=max(left,charmap[ch]+1)
            charmap[ch]=right
            max_len=max(max_len,right-left+1) 
        return max_len