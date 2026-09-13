class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1 : return nums[0]

        max_array = [1 if nums[0]==0 else nums[0]]*len(nums)
        min_array = [1 if nums[0]==0 else nums[0]]*len(nums)

        res = nums[0]

        for i in range(1,len(nums)):
            if nums[i]==0 : 
                max_array[i]=min_array[i]=1

            max_array[i] = max(nums[i],max_array[i-1]*nums[i], min_array[i-1]*nums[i])
            min_array[i] = min(nums[i],max_array[i-1]*nums[i], min_array[i-1]*nums[i])

            res = max(res,max_array[i])

        return res

