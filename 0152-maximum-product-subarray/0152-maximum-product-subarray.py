class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax=nums[0]
        curmin=nums[0]
        max_prd=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
                curmax,curmin=curmin,curmax
            curmax=max(n,curmax*n)
            curmin=min(n,curmin*n)
            max_prd=max(max_prd,curmax)
        return max_prd