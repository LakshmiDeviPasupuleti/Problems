class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in seen:
                return [seen[com],i]
            seen[nums[i]]=i