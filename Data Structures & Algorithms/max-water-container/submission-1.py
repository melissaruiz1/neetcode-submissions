class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the amount of water a container can store is equal to the distance (i -j)
        # * min height (heights[i], heights[j])

        # we can use a greedy appraoch here because once we check one area and find
        # the larger of the two, there won't be a larger area from that minimum height.

        left = 0
        right = len(heights) - 1

        max_area = 0

        while left < right:
            curr_area = (right - left) * min(heights[right], heights[left])
            max_area = max(max_area, curr_area)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_area