class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We can identify a starting sequence if it does not have a left neighbor
        # Once we identify the left neighbor, we continue calculating the length by 
        # searching for the existence of the a right neighbor. 
        # We recalculate the max length everytime 
        # We can iterate through the set to prevent searching through duplicates

        # [2, 20, 4, 10, 3, 4, 5]
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                i = num
                curr_length = 1
                while i + 1 in nums_set:
                    curr_length += 1
                    i += 1
                max_length = max(max_length, curr_length)

        return max_length
                
