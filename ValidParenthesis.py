class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parens = { '(' : ')', '{' : '}', '[' : ']' }
        
        for i in s:
            if i in parens:
                stack.append(parens[i])
                
            else:
                if len(stack)==0 or stack.pop()!=i:
                    return False
                
        return len(stack)==0