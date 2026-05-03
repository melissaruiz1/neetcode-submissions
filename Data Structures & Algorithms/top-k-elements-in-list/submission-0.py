class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Convert nums to a Counter
        # Sort the counter by values, get the last k values
        
        ans = []
        nums_count = Counter(nums)
        
        bucket_sort_arr = [[] for _ in range(len(nums))]

        for num in nums_count:
            freq = nums_count[num]
            bucket_sort_arr[freq - 1].append(num)
        
        freq_count = 0
        for nums_arr in reversed(bucket_sort_arr):
            for num in nums_arr:
                ans.append(num);
                freq_count += 1
                if freq_count == k:
                    return ans

        return ans



