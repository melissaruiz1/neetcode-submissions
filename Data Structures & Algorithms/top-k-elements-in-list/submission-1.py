class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Convert nums to a Counter
        # Sort the counter by values, get the last k values
        
        nums_count = Counter(nums)
        buckets = [[] for _ in range(len(nums))]

        for num, freq in nums_count.items():
            buckets[freq - 1].append(num)
        
        ans = []
        for freq in range(len(buckets) - 1, -1, -1):
            for num in buckets[freq]:
                ans.append(num);
                if len(ans) == k:
                    return ans

        return ans



