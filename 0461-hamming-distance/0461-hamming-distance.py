class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        #X=bin(x)
        #Y=bin(y)
        target=x^y
        while target >0:
            if target%2==1:
                count=count+1
            target=target//2
        return count 
        