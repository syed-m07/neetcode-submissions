class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num] = 1 + count.get(num, 0) #dictionary.get(key, default_value)
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
            arr.sort()
        
        res=[]
        while len(res) < k:
            res.append(arr.pop()[1]) #returns the number not the frequency of the number
        return res
            
        