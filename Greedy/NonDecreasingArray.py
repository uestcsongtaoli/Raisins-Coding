# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/6 11:42 下午
@Author:     wz
@File:       NonDecreasingArray.py
@Decs:
"""

'''
question：
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。


示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
'''


class Solution():
    def __init__(self, array):
        self.array =  array


    def check_possibility(self):
        """
        该题的思路同样是从左到右遍历array，当每遇到一个array[i]<array[i-1]，必然都需要进行一次调整，使其符合非递减，遍历玩array后，得到至少要调整多少次，使其达到全局最优

        而问题就到了array[i]<array[i-1]时需要如何调整的问题，尤其时下文的情况2。
        Returns:

        """
        # 假设有array为：...i-2,i-1,i,i+1,... ，需要做调整的情况有几种：
        # 1、考虑array为： ...1, 4, 2, 3,... 有两种方法，a). 4 -> 2 正解，因为对于i的位置来说，在满足非递减原则下，其值越小越好，越容易满足i+1及其后面非递减的原则；b). 2 -> 4
        # 2、考虑array为： ...3, 4, 2, 3,... 只有一种方法，a). 2 -> 4 (虽然调整后i-1,i,i+1也不能满足非递减的原则，但是i-2,i-1,i三个元素必然需要调整一次值，所以改例子并不能在改变 1 个元素的情况下，使之变成一个非递减数列)


        N = len(array)
        count = 0
        for i in range(1, N):
            if array[i] < array[i - 1]:
                count += 1
                if i == 1 or array[i] >= array[i - 2]: # short-circuit or
                    array[i - 1] = array[i]
                else:
                    array[i] = array[i - 1]
            print(array)
        return count <= 1


if __name__ == "__main__":
    array = [3, 4, 2, 1, 8, 7]

    solution = Solution(array)
    print(solution.check_possibility())
