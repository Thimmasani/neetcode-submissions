class Solution:
    def rob(self, nums: List[int]) -> int:
        temp = [0]+nums
        for i in range(2,len(temp)):
            temp[i] = max((temp[i]+temp[i-2]), temp[i-1])
        return temp[-1]