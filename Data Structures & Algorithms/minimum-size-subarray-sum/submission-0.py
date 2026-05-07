class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # start both pointers at 0
        # always expand right pointer
        # if sum is less than target, continue to expand
        # if sum is greater than target, shrink

        min_sub_len = math.inf
        left = 0

        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_sub_len = min(min_sub_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        if min_sub_len == math.inf:
            return 0
        else:
            return min_sub_len

