class Solution:
    def climbStairs(self, n: int) -> int:
        ways_list = [1]*(n+1)
        for i in range(2,n+1):
            ways_list[i] = ways_list[i-1]+ways_list[i-2]
        return ways_list[n]