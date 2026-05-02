class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Create an empty hashmap of nums with key: element value and value: index
        # 2. Loop through nums
        #   a. if  target - nums[i] is in the hashmap   
        #       i. return index i and the index from the hashmap
        #       ii. index from the hashmap needs to be returned first, then i
        #   b. if not in the hashmap, add to the hashmap and the other complement will
        #       find it later if it exists
        # 3. Return [-1, -1] after loop in case nothing was found


        # [ 4, 2, -1, 6]     target = 5
        complements = defaultdict(int)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                return [complements[complement], i]
            else:
                complements[nums[i]] = i
        return [-1, -1]