class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        n=len(s)
        if n%2!=0:
            return False
        mapping={")":"(","]":"[","}":"{"}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char]!=top:
                    return False
            else:
                stack.append(char)
        return not stack

        