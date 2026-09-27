class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        #count=0
        freq=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count=count+1
            freq.append(count)
        return freq
