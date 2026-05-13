class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        top_k = []
        for i in range(len(nums)):
            buckets.append(list())
        
        nums_count = Counter(nums)

        for key,val in nums_count.items():
            buckets[val - 1].append(key)

        for i in range(len(buckets) -1, -1, -1):
            if len(top_k) >= k:
                continue 
            if len(buckets[i]) == 0:
                continue
            else:
                top_k.extend(buckets[i])

        return top_k
            




        