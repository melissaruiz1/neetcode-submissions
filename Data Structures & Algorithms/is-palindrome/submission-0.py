class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sanitized_arr = []
        for ch in s:
            if ch.isalnum():
                sanitized_arr.append(ch.lower())
        sanitized_str = "".join(sanitized_arr)

        left, right = 0, len(sanitized_str) - 1
        while left < right:
            print(left, right)
            if sanitized_str[left] != sanitized_str[right]:
                return False
            left += 1
            right -= 1

        return True