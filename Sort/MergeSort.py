# _*_ coding: utf-8 _*_
"""
@Date:       2021/4/28 11:56 下午
@Author:     wz
@File:       MergeSort.py
@Decs:
"""


class MergeSort:
    """
    naive sort algorithm
    时间复杂度：best:O(NlogN)  worst:O(NlogN) mean:O(NlogN)
    空间复杂度：O(N)
    属性：稳定
    """

    def __init__(self, nums):
        self.nums = nums

    def merge_sort(self, nums):
        '''
        归并排序非递归实现
        Args:
            nums:

        Returns:

        '''

        return nums

    def recursive_merge_sort(self, nums, res, start, end):
        """
        归并排序递归实现
        Args:
            nums:   原list
            res:    每层递归结果存放于辅助list
        Returns:

        """

        if start>=end:
            return nums

        # 拆分list （下标控制 逻辑拆分）在分布式大规模排序中进行物理拆分
        mid = start + (end - start) // 2 # (start + end) >> 1 与 start + (end - start) >> 1 不同在于，当start + end可能超过Integer.MAX
        start1, end1 = start, mid
        start2, end2 = mid + 1, end

        self.recursive_merge_sort(nums, res, start1, end1)
        self.recursive_merge_sort(nums, res, start2, end2)

        # 合并nums[start1:end1+1]和nums[start2:end2+1]
        k = start
        while start1<=end1 and start2<=end2:
            if nums[start1] <= nums[start2]:
                res[k] = nums[start1]
                start1 += 1
            else:
                res[k] = nums[start2]
                start2 += 1
            k += 1

        while start1<=end1:
            res[k] = nums[start1]
            k += 1
            start1 += 1

        while start2<=end2:
            res[k] = nums[start2]
            k += 1
            start2 += 1

        # 将当前递归层结果从辅助list导回原list，供上层递归层使用
        for i in range(start, end + 1):
            nums[i] = res[i]
        return nums


if __name__ == "__main__":

    nums = [1,4,7,1,3,7,9,2,0,3]
    res = len(nums) * [0]
    start, end = 0, len(nums) - 1
    sort = MergeSort(nums)

    print("归并排序结果为: {}".format(sort.recursive_merge_sort(nums, res, start, end)))