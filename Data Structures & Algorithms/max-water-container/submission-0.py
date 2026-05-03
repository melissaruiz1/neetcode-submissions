class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = l * h
        # create two pointers, start and end of the array
        # calculate area
        # if right pointer is larger than left pointer, increase right pointer
        # if left pointer is larger than right pointer, decrease right pointer


        # 1. initialize max_area to 0
        # 2. initialize pointers
        # 3. while left < right
        #   a. calculate the area at left right
        #   b. calculate which pointer is larger and increment / decrement accordingly
        #   c. calculate max area
        # return max area

        max_area = 0
        left, right = 0, len(heights) - 1


        while left < right:
            curr_area = (right - left) * min(heights[left], heights[right]) 
            max_area = max(max_area, curr_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        