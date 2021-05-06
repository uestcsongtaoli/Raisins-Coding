# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/2 4:36 下午
@Author:     wz
@File:       Candy.py
@Decs:
"""

'''
question:
一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，规则是如果一个孩子的评分比自己身旁的一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果；
所有孩子至少要有一个糖果。求解最少需要多少个糖果。

examples:
输入是一个数组，表示孩子的评分。输出是最少糖果的数量。
Input: [1,0,2]
Output: 5
'''


class Solution():
    def __init__(self, children):
        self.children =  children


    def candy(self):

        '''
        需要考虑从左向右和从右向左两个维度，当两者同时考虑时会有所疏漏，需要分别考虑，两次贪心完成
        Returns:

        '''
        children = self.children
        # 先初始化每个小孩一块糖果
        nums = [1] * len(children)
        print("children:", children)

        # 这里显然一次循环不足以同时考虑左边右边孩子的得分关系，需要在每次循环找到其极限下的局部最优，即每次循环确定一个方向上的大小关系，对应给孩子糖果
        for i in range(0, len(children)-1):
            if children[i] < children[i + 1]: # 只处理了 children[i] < children[i+1]的case
                nums[i + 1] = nums[i] + 1 # 贪心同时表现在每次只多给1块糖果
        print("left->right candy: ", nums)


        for i in range(len(children)-1, 0, -1):
            if children[i] < children[i - 1]: # 只处理了 children[i-1] > children[i+1]的case
                nums[i - 1] = max(nums[i] + 1, nums[i - 1])
                # 取max的缘由 (或者在if内加 nums[i] + 1 > nums[i - 1] 条件)：
                # children: [1,2,3,4,5,0]
                # left->right candy: [1,2,3,4,5,1]
        print("right->left candy: ", nums)
        # 两次循环均为考虑相邻children相等的case，因题意未提到相等时的处理逻辑故不做处理。
        # 当对相等时有分配糖果的要求时，如要求相邻孩子分数相等时，因为left->right 或 right->left都需要对相等情况做操作，存在冲突，可能需要额外循环处理。

        number = sum(nums)
        return number



if __name__ == "__main__":
    children = [1,6,6,6,4,2,4,2,7,5,100]

    solution = Solution(children)
    print(solution.candy())
