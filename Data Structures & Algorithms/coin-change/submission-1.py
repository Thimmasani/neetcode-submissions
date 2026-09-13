class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [amount+1]*(amount+1)
        res[0] = 0

        for i in range(1,len(res)):
            for coin in coins:
                if i<coin: continue
                else: res[i] = min(1+res[i-coin],res[i])

        if res[amount]== (amount+1) : return -1
        else: return res[amount]


        