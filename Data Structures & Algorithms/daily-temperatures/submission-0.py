class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []


        for i in range(0, len(temperatures)):
            count = 0
            found= False
            while(i + count + 1 < len(temperatures)):
                if temperatures[i] < temperatures[i+count+1]:
                    result.append(count+1)
                    found = True
                    break
                else:
                    count+=1
            if not found:
                result.append(0)
            
        return result
