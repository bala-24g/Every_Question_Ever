class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
     
        ptr=0

    
        while ptr<len(s):
            if stack and (stack[-1]=="(" and s[ptr]==")"):
                stack.pop()
            else:
                stack.append(s[ptr])
            ptr+=1
        return len(stack)

#Very much like valid parantheses.