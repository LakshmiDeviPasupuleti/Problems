class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=0
        a=0
        l=0
        o=0
        n=0
        for ch in text :
            if ch=='b':
                b=b+1
            elif ch=='a':
                a=a+1
            elif ch=='l':
                l=l+1
            elif ch == 'o':
                o += 1
            elif ch == 'n':
                n += 1
        l=l//2
        o=o//2
        return min(b,a,l,o,n)