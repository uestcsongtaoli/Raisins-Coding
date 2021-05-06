# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/5 4:34 下午
@Author:     wz
@File:       BestTimeToBuyAndSellStock2.py
@Decs:
"""

'''
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


示例:
输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

输入: prices = [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''


class Solution():
    def __init__(self, prices):
        self.prices =  prices

    '''
    根据此题的题意，说明可以在卖出当日，同时进行买入，且并没有要求给出进行交易的时间，所以可以把问题转变成子问题：每天是否进行交易，进行是否有纯收益。
    如果有一个交易需要在 prices[2]买入，prices[5]卖出，则 prices[5] - prices[2] = prices[5]-prices[4] + prices[4]-prices[3] + prices[3]-prices[2] 
    当每天的交易纯收益（子问题）达到最大时，问题到达最大。即可贪心解决
    
    当然能分析到这里，说明此问题也可动态规划解。
    '''
    def best_time_maximum_profit(self):

        prices = self.prices
        profit = 0.0

        for i in range(len(prices) - 1):
            profit += max(0, prices[i+1] - prices[i]) # 每天的最大收益

        return profit

    '''
    如上面的分析，也可以换成动态规划的思路做这道题。
    dp[i][0]:表示第i天时，且当前未持有股票的收益情况 
    dp[i][1]:表示第i天时，且当前持有股票的收益情况 
    则有如下两个dp公式：
    dp[i][0] = max{dp[i-1][0], dp[i-1][1] + prices[i]} # 分别表示前一天也未持有股票，和前一天持有股票并在今天把股票卖出
    dp[i][1] = max{dp[i-1][0] - prices[i], dp[i-1][1]} # 分别表示前一天也未持有股票并买入当天股票，和前一天已持有股票
    '''
    def best_time_maximum_profit_dp(self):

        prices = self.prices
        profit = 0.0

        # 这里有一个python的小坑，直接用乘号创建多维list，第一个乘号正常，但第二个乘号" * len(prices)"存在浅拷贝，只是分配了指针而没有内存的问题，故创建多维数组需要使用列表推到式
        # dp = [ [0.]*2 ] * len(prices)
        dp = [[0. for i in range(2)] for j in range(len(prices))] # dp这里把保证每天纯利润最大的前提下，纪录每天的收益

        dp[0][0] = 0.0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])

        profit = max(dp[len(prices)-1][0], dp[len(prices)-1][1])

        return profit



if __name__ == "__main__":
    prices = [3,6,1,6,2,2,2,7,9]

    solution = Solution(prices)
    print(solution.best_time_maximum_profit())
    print(solution.best_time_maximum_profit_dp())