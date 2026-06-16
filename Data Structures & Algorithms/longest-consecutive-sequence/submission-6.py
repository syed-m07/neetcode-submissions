class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 0
        numSet = set(nums)  #we're using set for O(1) lookup for elements, sorting takes 0(n logn) time

        for n in numSet:
            if n - 1 not in numSet:
                length=1

                while n + length in numSet:
                    length+=1
                
                longest = max(length, longest)
        
        return longest