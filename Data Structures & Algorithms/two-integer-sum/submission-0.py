class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,val in enumerate(nums):
            if (val) in hashmap: return [hashmap[val],i]
            else : hashmap[target-val]=i
