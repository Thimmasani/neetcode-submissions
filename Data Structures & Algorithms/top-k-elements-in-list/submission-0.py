from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = Counter(nums)
        return [x[0] for x in sorted(counter_dict.items(),key = lambda item:item[1], reverse=True)[:k]]