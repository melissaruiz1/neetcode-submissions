class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                last_lowest_temp_idx = stack.pop()
                results[last_lowest_temp_idx] = i - last_lowest_temp_idx
            
            stack.append(i)
        return results