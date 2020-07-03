class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        maxprofit = 0
        for cur_price in prices:
            if cur_price < minprice:
                minprice = cur_price
            else:
                maxprofit = max(maxprofit, cur_price - minprice)
        return maxprofit
