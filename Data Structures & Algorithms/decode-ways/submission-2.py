class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1              # empty prefix — 1 way (base case, "do nothing")
        dp[1] = 1              # s[0] != '0', already checked above, so 1 way

        for i in range(2, n + 1):
            one = int(s[i-1]) != 0                        # last single digit valid?
            two = 10 <= int(s[i-2:i]) <= 26                # last two digits valid?

            if one:
                dp[i] += dp[i-1]
            if two:
                dp[i] += dp[i-2]

            if dp[i] == 0:
                return 0   # stuck — no way to decode up to this point

        return dp[n]