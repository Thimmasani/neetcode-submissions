class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)==1 : return [0]
        res = [0]*len(temperatures)
        stack = []

        for i,val in enumerate(temperatures):
                while stack and (val > stack[-1][1]):
                    res[stack[-1][0]]= i - stack[-1][0]
                    stack.pop()
                
                stack.append([i,val])

        return res

            
