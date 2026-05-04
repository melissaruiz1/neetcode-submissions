class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open_chars = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for ch in s:
            if ch in closed_to_open_chars:
                if not stack or stack[-1] != closed_to_open_chars[ch]:
                    return False
                
                if stack and stack[-1] == closed_to_open_chars[ch]:
                    stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0