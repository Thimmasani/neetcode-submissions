from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        test = sorted(Counter(nums).items(), key= lambda x:x[1], reverse=True)
        result=[]
        for i in range(k):
            result.append(test[i][0])
        return result
