class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # looking for the longest substring with at most "k" different characters
        # from the current window's "most" characters

        # constraint metric: longest subarray
        # constraint numeric: k characters that are different than the most characters
        # in a subarray


        # AAABCA k = 2
        # brute force: we can use a map to determine what the most seen character currently
        # is, then loop through every single subarray to get the "longest" subarray
        # that only has k more characters

        # we could use a sliding window technique:
        # 0a. initialize an empty Counter
        # 0b. initialize the max to 0
        # 0c. initialize left to 0, right will be initialize in the loop since we'll always
        #   iterate. 

        # 1. start both pointers at the first element and add the right element counter to 
        #   the Counter
        # 2. while the number of chars (keys) is greater than k + 1, increase the left pointer
        # 3. re-calculate the max by the current right - left + 1
        # 4. return the max

        # A A A B A B B       k = 1
        # L R
        # char_counts = {A: 2}
        # longest_substr_len = 1
        char_counts = Counter()
        longest_substr_len = 0
        left = 0

        for right in range(len(s)):
            char_counts[s[right]] += 1

            while sum(char_counts.values()) - max(char_counts.values()) > k:
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    del char_counts[s[left]]
                left += 1
            longest_substr_len = max(longest_substr_len, right - left + 1)
        return longest_substr_len

