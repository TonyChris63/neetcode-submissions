class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posTime = {}
        fleet = 1
        stack = []

        if not position:
            return 0
        
        for i in range(len(position)):
            posTime[position[i]] = (target - position[i])/speed[i]
        
        position.sort()

        for p in position:
            stack.append(posTime[p])
        
        start = stack.pop()

        while stack:
            if start >= stack[-1]:
                stack.pop()
            else:
                fleet += 1
                start = stack.pop()

        return fleet