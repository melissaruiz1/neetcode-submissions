class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # constraint metric: number of unique characters
        # numeric constraint: at most 1 unique character 

        # 0a. Initialize max_substring_len to 0
        # 0b. Initialize left pointer
        # 0c. Initialize empty counter map
        # 1.  Loop through the right pointer, starting at 0
        #   a. Add current element to set
        #   b. While length of the set is greater than the length of window,
        #       remove element from set and increase left pointer
        #   c. Recalculate max_substring_len based on current window size
        # 2. Return max_substring_len

        # " z x y z x y "
        #     L   R 

        # max_substr_len = 3
        # unique_chars_count = {z: 1, x: 1, y: 1}
        unique_chars_count = Counter()
        max_substr_len = 0

        left = 0
        for right in range(len(s)):
            unique_chars_count[s[right]] +=1
            while len(unique_chars_count) != (right - left + 1):
                unique_chars_count[s[left]] -= 1
                if unique_chars_count[s[left]] == 0:
                    del unique_chars_count[s[left]]
                left += 1

            max_substr_len = max(max_substr_len, right - left + 1)
        return max_substr_len

        # time complexity: O(n)
        # space complexity: O(n)