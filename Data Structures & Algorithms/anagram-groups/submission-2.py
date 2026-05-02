class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through the array 
        # anagrams all have the same Counter structure
        # somehow lookup current string to see if anagram structure exists, then append
        # it to the value array. 
        # Counters / dicts can NOT be hashed
        # We CANNOT use the ASCII value code since "ac" and "d" would be considering anagrams
        # when they're not
        # We can instead create an array of size 26 prefilled with 0's, and add the character
        # count to their ASCII value on the array
        # convert the array to a tuple for hashing

        # 0a. Initialize an empty list to append to
        # 0b. Initialize an empty dict for lookup of type list
        # 1. Loop through strs. For each string:
        #   a. Convert to a hashable anagram code
        #   b. If that code exists in the hash map
        #       i. Append the raw string to the hashmap's list
        #   c. If it does not exist, add the code as the key and append the raw string
        #       to the value 
        # 2. Loop through the values of the hashmap and append each array individuall to 
        #   the empty array
        # Return the array

        # ["ac","c"]
        grouped_anagrams = []
        anagram_counts = defaultdict(list)

        for anagram in strs:
            anagram_list = [0] * 26
            for ch in anagram:
                ch_index = ord(ch) - ord('a')
                anagram_list[ch_index] += 1
            anagram_tuple = tuple(anagram_list)
            anagram_counts[anagram_tuple].append(anagram)

        for anagrams_arr in anagram_counts.values():
            grouped_anagrams.append(anagrams_arr)
        
        return grouped_anagrams

