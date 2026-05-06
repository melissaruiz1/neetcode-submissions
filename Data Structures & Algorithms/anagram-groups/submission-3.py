class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through each string
        # convert to a tuple using a size 26 array and counts
        # add tuple to hashmap where the list of the raw strings are appended to
        # loop through the values to append to an answer array and return

        grouped = []

        anagrams_map = defaultdict(list)

        for s in strs:
            str_count = [0] * 26
            for ch in s:
                ch_idx = ord(ch) - ord('a')
                str_count[ch_idx] += 1
        
            anagrams_map[tuple(str_count)].append(s)
        
        for anagrams in anagrams_map.values():
            grouped.append(anagrams)
        
        return grouped