class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            store=nums[nums[i]]
            ans.append(store)
        return ans