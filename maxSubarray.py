class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = current_sub = nums[0]

        for i in nums[1:]:

            current_sub = max(i,current_sub + i)

            max_sub = max(max_sub,current_sub)

            
        return max_sub    


        
