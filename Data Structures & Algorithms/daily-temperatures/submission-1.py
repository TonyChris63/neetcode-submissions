class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        enumerate(temperatures)
        stack = []
        res = [0] * len(temperatures)

        for i, tem in enumerate(temperatures):
            if not stack:
                stack.append([i, tem])
            elif stack and tem > stack[-1][1]:
                while stack and tem > stack[-1][1]:
                    days = i - stack[-1][0]
                    res[stack[-1][0]] = days
                    stack.pop()
                stack.append([i, tem])
            else:
                stack.append([i, tem])
        
        return res

