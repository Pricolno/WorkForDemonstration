class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n_size = len(prices)
        max_suff = [0 for _ in range(n_size)]
        max_suff[-1] = prices[-1]
        for ind in range(n_size - 2, -1, -1):
            max_suff[ind] = max(max_suff[ind + 1], prices[ind])
        
        ans = 0
        for ind in range(n_size - 1):
            buy_price = prices[ind]
            sell_price = max_suff[ind + 1]

            ans = max(ans, sell_price - buy_price)
        
        if ans == 0:
            return 0
        else:
            return ans