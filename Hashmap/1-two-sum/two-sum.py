class Solution:
    def twoSum(self,nums,target):
        mp={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in mp:
                return [mp[x],i]
            mp[nums[i]]=i