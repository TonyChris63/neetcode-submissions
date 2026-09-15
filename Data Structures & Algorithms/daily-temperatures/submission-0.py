class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = enumerate(temperatures)
        stack = []
        res = [0] * len(temperatures)

        for i,t in t:
            while stack and t > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i,t))
        return res
        
