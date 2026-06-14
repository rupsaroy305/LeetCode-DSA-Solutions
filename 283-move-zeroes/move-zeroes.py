class Solution:
    def moveZeroes(self, nums):
        write = 0
        
        # move all non-zeros forward
        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1
        
        # fill remaining with zeros
        for i in range(write, len(nums)):
            nums[i] = 0