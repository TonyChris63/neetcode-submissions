class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        posTime = {}
        fleet = 1

        if not position:
            return 0

        for i in range(len(position)):
            posTime[position[i]] = (target - position[i])/speed[i]
        
        print(posTime)
        position.sort()

        for n in position:
            stack.append(n)

        start = stack.pop()
        
        while stack:
            if posTime[start] >= posTime[stack[-1]]:
                stack.pop()
            else: 
                fleet += 1
                start = stack.pop()

        return fleet



