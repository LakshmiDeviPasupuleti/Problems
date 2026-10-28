class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        minium=nums[0]
        for num in nums:
            if num < minium:
                minium=num
        return minium