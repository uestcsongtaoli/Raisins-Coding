# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/5 6:26 下午
@Author:     wz
@File:       QueueReconstructionByHeight.py
@Decs:
"""

'''
假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面正好有 ki 个身高大于或等于 hi 的人。
请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。

示例 1：

输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
解释：
编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。

'''


class Solution():
    def __init__(self, people):
        self.people = people

    '''
    这题着实秀到我了... 包括return等，5行解决了
    
    这题和Candy题类似，都是有两个衡量维度，每次去解决一个维度上的问题。
    Candy题中有 从左往右 和 从右往左 两种排序
    此题有 身高 和 前面有多少大于等于身高 两个维度进行排序
    '''

    def queue_reconstruction(self):

        people = self.people
        queue = []

        # ki维度
        people = sorted(people, key=lambda x:(x[0], -x[1]), reverse=True) # 按hi从高到低排好序，且在同一个高度hi下的ki是相对有序的
        print(people)

        for i in people:
            # 因遍历排好序的people过程中，取到的当前的hi永远小于等于queue内的hi，并且ki越小越先取到，所以对于当前的[hi, ki]，结合ki定义，ki就是其插入的位置
            queue.insert(i[1], i) # 遍历的时候将当前元素插入到ki维度内，每次插入过程都是局部最优解，最终插入完成达到全局最优

        return queue



if __name__ == "__main__":
    prices = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

    solution = Solution(prices)
    print(solution.queue_reconstruction())
