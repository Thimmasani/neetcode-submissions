class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = cost + [0]

        for i in range(2,len(total_cost)):
            total_cost[i] += min(total_cost[i-1],total_cost[i-2])
        
        return total_cost[-1]


