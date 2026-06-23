'''
Monotonic stack approach O(n)-> monotonic means that the elements either increase or stay the
                                same value OR they decrease or stay the same value as we go 
                                left to right
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        return result