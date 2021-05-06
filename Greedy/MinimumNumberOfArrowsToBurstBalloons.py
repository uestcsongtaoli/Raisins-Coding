# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/3 4:16 下午
@Author:     wz
@File:       MinimumNumberOfArrowsToBurstBalloons.py
@Decs:
"""


'''
question:
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。

Example:
Input:
[[10,16], [2,8], [1,6], [7,12]]
Output:
2

对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
'''

class Solution():
    def __init__(self, points):
        self.points =  points


    def minimum_number_of_arrows(self):

        # 与NonOverlappingIntervals题很像，区间规划问题无非三板斧。
        # 贪心思路：每颗气球都至少需要一支箭，每支箭需要尽可能多地射中气球，故就变成了排好序选中一个区间，当两个区间有重叠时，可一支箭搞定。
        # 故问题变成当区间两两之间都有交集时，则合并区间，问最后区间一共有多少个 ？

        # 按区间终止位置升序排序
        points = sorted(self.points, key=lambda x:x[1])
        print(points)
        count = 1

        end = points[0][1]
        for i in range(len(points)): # 贪心在 想一支箭尽量射中可能多的气球
            if points[i][0] > end: # 当满足这一区间起始位置 > 上一区间终止位置时，两者无交集，则count++
                count += 1
                end = points[i][1]
                print(points[i])

        # # 按区间开始位置升序排序
        # points = sorted(self.points, key=lambda x: x[0])
        # print(points)
        # count = 1
        #
        # end = points[0][1]
        # for i in range(len(points)):
        #     if points[i][0] > end:
        #         count += 1
        #         end = points[i][1]
        #         print(points[i])
        #     else:
        #         end = min(end, points[i][1])  # 被合并区间两两之间都要有交集才能可以合并，所以有取min这一操作，每次在合并后，验证是否需要缩短结束区间长度

        return count



if __name__ == "__main__":
    # points = [[1,3],[3,5],[2,7],[2,2],[2,3],[5,8],[7,8]]
    points = [[1, 5], [4, 7], [0, 8], [11, 11], [13, 13], [9, 14], [10, 15], [16, 19], [20, 20], [21, 21], [17, 22], [18, 23]]

    solution = Solution(points)
    print(solution.minimum_number_of_arrows())