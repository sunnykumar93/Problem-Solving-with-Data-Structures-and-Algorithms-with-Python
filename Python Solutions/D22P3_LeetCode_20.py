# Python3 code coming soon
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()

        
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            elif len(stack)>0:
                if stack[-1]=="{" and i=="}":
                    stack.pop()
                elif stack[-1]=="[" and i=="]" :
                    stack.pop()
                elif stack[-1]=="(" and i==")":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
                
        print(stack)
        return (len(stack)==0)
             
