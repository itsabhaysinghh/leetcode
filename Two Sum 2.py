class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0 
        right = len(nums)-1

        while left < right:
            x = nums[left] + nums[right]
            
            if x == target:
                return [left+1,right+1]


            elif x > target:

                right -=1

            else:

                left+=1        
        
