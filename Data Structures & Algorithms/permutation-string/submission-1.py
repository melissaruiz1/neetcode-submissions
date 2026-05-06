class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # perimutation means same characters, any order
        # in order for it to be a permutation in another string, it must:
            # 1. include all characters
            # 2. characters must be adjacent to each other
            # 3. characters can be in any order

        # brute force: convert s1 into an object
        # loop through all subarrays of size len(s2), convert to a Counter, then 
        # compare Counters. 

        # optimal: fixed window sliding window

        #1. start left pointer at 0, start right pointer at len(s1) - 2 or len(s1)
        # 0a. Initialize s1 counter,and s2 counter with the len(s1)characters
        # 0b. Initialize left pointer to 0
        # 1. Add right character to Counter
        # 1. Loop right starting at len(s1) - 1 to the end of the array
        # 2. If s2 counter == s1 counter, retrn True early
        # 3. Else, increment left and remove it from Counter

        # s1 = "ab", s2 = "lecabee"
        s1_counts = Counter(s1)
        s2_counts = Counter(s2[:len(s1) - 1])

        left = 0
        k = len(s1) - 1
        for right in range(k, len(s2)):
            s2_counts[s2[right]] += 1
            if s1_counts == s2_counts:
                return True
            s2_counts[s2[left]] -= 1
            if s2_counts[s2[left]] == 0:
                del s2_counts[s2[left]]
            left += 1
        return False