class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [nums[0]]
        for i in range(1,n):
            x = arr[i-1] + nums[i]
            arr = arr + [x]
       
        return arr
