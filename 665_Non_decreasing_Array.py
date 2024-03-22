class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decreasing_count = 0
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  
                decreasing_count += 1
                
                if decreasing_count > 1:
                    return False
                
                if i == 0 or i == len(nums) - 2 or nums[i - 1] <= nums[i + 1] or nums[i] <= nums[i + 2]:
                    continue
                else:
                    return False
        
        return True
