class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        iter1 = [0,0]+nums[1:]
        iter2 = [0]+nums[:-1]+[0]
        for i in range(2, len(iter1)):
            iter1[i] = max(iter1[i]+iter1[i-2], iter1[i-1])
            iter2[i] = max(iter2[i]+iter2[i-2], iter2[i-1])
        return max(iter1[-1], iter2[-1]) 