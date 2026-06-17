class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing_map = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in closing_map:
                if not stack or stack[-1] != closing_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack)==0