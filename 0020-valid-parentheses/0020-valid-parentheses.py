class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brac={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in brac:
                if stack and stack[-1] == brac[ch]:
                    stack.pop()
                else :
                    return False
            else:
                stack.append(ch)
        return len(stack)==0
            
