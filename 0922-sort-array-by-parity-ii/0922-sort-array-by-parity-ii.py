class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        res=[]
        even=[]
        odd=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for i in range(len(nums)):
            if i%2==0:
                res.append(even[i//2])
            else:
                res.append(odd[i//2])
        return res