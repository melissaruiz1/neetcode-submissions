class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 0. Initialize output array with [1] * len(nums)
        # 1. loop through nums once, and calculate prefix product starting at index 1
        # 2. loop through nums again in reverse, calculate postfix sum starting at index len(nums) - 1
        # return ouput array

        # [1, 1, 1, 1]
        arr = [1] * len(nums)

        curr_prefix_prod = 1
        for i in range(len(nums)):
            curr_prefix_prod *= nums[i]

            if i < len(nums) - 1: 
                arr[i + 1] = curr_prefix_prod

        curr_postfix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            curr_postfix_prod *= nums[i]

            if i > 0:
                arr[i - 1] *= curr_postfix_prod
            
        return arr




