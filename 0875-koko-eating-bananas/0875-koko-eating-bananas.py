class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low < high :
            mid=(low+high)//2
            hour=0
            for p in piles :
                hour=hour+(p+mid-1)//mid
            if hour <= h:
                high=mid
            else:
                low=mid+1
        return low
        
        