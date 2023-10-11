class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, value in enumerate(nums): 
            rem = target - nums[i] 
           
            if rem in pos: 
                return [pos[rem], i] 
            else:
                pos[value] = i  
            
