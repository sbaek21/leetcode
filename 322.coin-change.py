#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1] * (amount+1)
        # amount + 1 is a value that is greater than the maximum possible number of coins required
        
        dp[0] = 0 # base case

        """
        equivalent as
        dp = []
        for i in range(amount+1):
            dp.append(amount+1)
            
        dp[0] = 0
        -------
        example: amount = 11
        dp = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        idx    0   1   2   3   4   5   6   7   8   9  10  11
        """

        
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1+dp[a-coin])
        return dp[amount] if dp[amount] != amount + 1 else -1
                
# @lc code=end

