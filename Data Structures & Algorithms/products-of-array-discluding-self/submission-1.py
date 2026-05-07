class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we want to use prefix product and place it in the the cell we want to calculate
        # (so every i + 1 and skip the first element since it doesn't have a prefix product)

        # then once we add the prefix product to the output array, we are going to 
        # iterate through it in reverse to multiply by the postfix product.
        # the postfix product will also be i + 1 starting from the last element, since
        # the last element doesn't have a postfix product


        # nums: [1, 2, 4, 6]

        # prefix array = [1, 1, 2, 8]

        # postfix: [48, 24, 6, x]

        # output: [48, 24, 12, 8]

        # 1. initialize output array to be [1] * len(nums)
        # 2. Loop through nums and append to the output array starting at (i + 1)
        # 3. Loop through nums in reverse, 
        #    multiply the result by the answer in i starting at i + 1 of the reverse output array

        # return output array

        # [1 , 1, 1, 1]
        output = [1] * len(nums)

        # [1, 1, 2, 8]
        curr_prefix = 1
        for i in range(1, len(nums)): 
            curr_prefix *= nums[i-1]
            output[i] = curr_prefix

        # [1, 1, 2, 8]        
        curr_postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            curr_postfix *= nums[i+1]
            output[i] *= curr_postfix

        return output

        

