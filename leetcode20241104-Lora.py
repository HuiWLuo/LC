# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {')':'(',']':'[','}':'{'}

        for c in s:
            if c in  closetoopen.values():
                stack.append(c)
            elif c in closetoopen.keys():
                if not stack or closetoopen[c] != stack.pop():
                    return False
                
        return not stack

  # 394. Decode String
  class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string=''
        k = 0
        for i in s:
            if i=="[":
                stack.append(string)
                stack.append(k)
                string=""
                k=0
            elif i=="]":
                stack_num=stack.pop()
                prev_string=stack.pop()
                string=prev_string+stack_num*string
            elif i.isdigit():
                k=k*10 + int(i)
            else:
                string+=i
        return string   

739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res 
