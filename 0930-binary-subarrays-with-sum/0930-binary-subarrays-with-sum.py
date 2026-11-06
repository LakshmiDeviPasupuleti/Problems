class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        hashmap={0:1}
        sum=0
        count=0
        for i in range(len(nums)):
            sum +=nums[i]
            remain=sum-goal
            if remain in hashmap:
                    count+=hashmap[remain]
            hashmap[sum]=hashmap.get(sum,0)+1  
        return count          
            
                