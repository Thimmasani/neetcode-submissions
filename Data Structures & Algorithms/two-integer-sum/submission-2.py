class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_dict = {}
        for i in range(len(nums)):
            if (target-nums[i]) in value_dict: return [value_dict[target-nums[i]],i]
            else: value_dict[nums[i]]=i