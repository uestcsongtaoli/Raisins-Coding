# _*_ coding: utf-8 _*_
"""
@Date:       2021/4/29 10:54 上午
@Author:     wz
@File:       SelectSort.py
@Decs:
"""


class SelectSort():
    """
    naive sort algorithm
    时间复杂度：best:O(N^2)  worst:O(N^2) mean:O(N^2)
    空间复杂度：O(1)
    属性：不稳定
    """

    def __init__(self, nums):
        self.nums = nums

    def select_sort(self):

        # selectSort每轮外层循环确定一个最小or最大值位置，故最多进行len(self.nums)次循环
        for i in range(len(self.nums)):
            min = i
            # 纪录最小or最大值位置，且不需要对比已被确定的元素，故比较次数为 (n-1)*(n-2)/2 次
            for j in range(i + 1, len(self.nums)):
                if self.nums[j] < self.nums[min]:
                    min = j
            if min != i:
                self.nums[i], self.nums[min] =  self.nums[min], self.nums[i]

        return self.nums


if __name__ == "__main__":
    nums = [1,4,6,7,2,4,6,7,9,100]
    sort = SelectSort(nums)
    print(sort.select_sort())