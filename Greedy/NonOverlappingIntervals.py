# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/2 5:55 下午
@Author:     wz
@File:       NonOverlappingIntervals.py
@Decs:
"""


'''
question:
给定多个区间，计算让这些区间互不重叠所需要移除区间的最少个数。起止相连不算重叠。

Examples:
输入是一个数组，数组由多个长度固定为2的数组组成，表示区间的开始和结尾。输出一个整数，表示需要移除的区间数量。
Input: [[1,2], [2,4], [1,3]]
Output: 1
'''


class Solution():
    def __init__(self, intervals):
        self.intervals =  intervals


    def erase_overlap_intervals(self):

        # 此题刚拿到完全不知道该如何下手 - -
        # 首先要去掉多少个区间，就是问可以留下来的区间是哪些，共多少个
        # 那这个问题实际上是一个时间区间调度问题，大致有两种解决方案：1、动归(万物皆可动归) 2、贪心
        # 主要实现贪心方法：一个原则，选择区间的时候，为之后的区间留下更多的空间，最终达到该次操作的局部最优
        #               思路为，将区间按结束时间升序排好序后，依次遍历排好序的区间，选取可以选择的空间，保证留给之后的区间段最大即可，最终到全局最优解中的一个

        intervals = self.intervals

        # 按区间终止位置排好序
        intervals = sorted(intervals, key=lambda x:x[1])
        count = 1
        end = intervals[0][1]
        for interval in intervals: # 贪心在 永远想要使得剩下可选择区间最大的，但是只能选择符合下面条件的
            if interval[0] >= end: # 当下一个区间开始位置>=上一个区间结束位置，则为可以选择的区间
                end = interval[1]
                count += 1

        return len(intervals) - count

'''
note:
1、典型的区间问题，无非先排序（根据起始或终止位置升序or降序排序），再贪心迭代即可。
2、特殊的用扫描线 （待学习）
'''

if __name__ == "__main__":
    intervals = [[1,3],[3,5],[2,7],[3,7],[2,3],[5,8],[7,8]]

    solution = Solution(intervals)
    print(solution.erase_overlap_intervals())
