class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1 : return len(nums)
        num_set = set(nums)
        res = 1
        start_elements = set()
        for i in nums:
            if (i-1 in num_set) or (i+1 not in num_set) :  continue
            else:
                start_elements.add(i)
        
        for i in start_elements:
            curr_count=0
            curr_val = i
            while curr_val in num_set:
                curr_count += 1
                curr_val += 1
                res = max(res, curr_count)
        return res
        

        