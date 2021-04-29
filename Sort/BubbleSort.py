# _*_ coding: utf-8 _*_
"""
@Date:       2021/4/29 10:25 上午
@Author:     wz
@File:       BubbleSort.py
@Decs:
"""

class BubbleSort():

    """
    naive sort algorithm
    时间复杂度：best:O(N^2)  worst:O(N^2) mean:O(N^2)
    空间复杂度：O(1)
    属性：稳定
    """
    def __init__(self, nums):
        self.nums = nums


    def bubble_sort(self):

        # bubbleSort每轮外层循环确定一个最小or最大值位置，故最多进行len(self.nums)次循环
        for i in range(len(self.nums)):
            swap_flag = False
            # 内层循环确定相邻元素间的对比，且不需要对比已被确定的元素，故比较次数为 (n-1)*(n-2)/2 次
            for j in range(len(self.nums) - i - 1):
                if self.nums[j] > self.nums[j + 1]:
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]
                    swap_flag = True
            if not swap_flag:
                break

        return self.nums

if __name__ == "__main__":
    nums = [1,4,6,7,2,4,6,7,9,100]
    sort = BubbleSort(nums)
    print(sort.bubble_sort())
