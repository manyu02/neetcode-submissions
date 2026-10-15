class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=["+","-","*","/"]
        stack=[]
        for i in tokens:
            if i not in a:
                stack.append(i)
            if i in a:
                second=int(stack.pop())
                first=int(stack.pop())
                if i=="+":
                    new= first+second
                if i=="-":
                    new=first-second
                if i=="*":
                    new=first*second
                if i=="/":
                    new=first/second
                stack.append(new)
        return int(stack[-1])

        