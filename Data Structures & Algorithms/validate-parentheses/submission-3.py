class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        # "([{}])"
        stack = []
        for ch in s:
            if ch in mapping:
                if stack and mapping[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
            
