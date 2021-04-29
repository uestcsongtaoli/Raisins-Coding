# _*_ coding: utf-8 _*_
"""
@Date:       2021/4/28 11:45 下午
@Author:     wz
@File:       HeapSort.py
@Decs:
"""


class Heap():
    """
    naive sort algorithm
    时间复杂度：best:O(NlogN)  worst:O(NlogN) mean:O(NlogN)
    空间复杂度：O(1)
    属性：不稳定


    heap的初始化是一个从第一个非叶子节点直到根节点的自上而下的调整过程；
    heap的pop是一个只有根节点的自上而下的调整过程；
    heapSort是一个反复将堆顶元素pop的过程，继而使list有序
    heap的push是一个从堆底自下而上的调整过程

    key：heap的关键时自上而下和自下而上的调整

    more：heap是一个很有用的dataStructure eg: priority_queue / topK 问题
    """

    def __init__(self, nums):
        self.nums = nums


    def heapify(self):

        index = ((len(self.nums) - 1) - 1) // 2

        # 从第一个不是叶子节点的节点开始往前（对应索引越来越小）调整至根节点
        while index>=0:
            print("当前父节点索引为{}，值为{}；对应nums为{}".format(index, self.nums[index], self.nums))
            self.shift_down(index)
            print("调整后，当前父节点索引为{}，值为{}；对应nums为{}".format(index, self.nums[index], self.nums))
            print("----------------------------------")
            index -= 1


    def push(self, value):
        self.nums.append(value)
        self.shift_up()


    def pop(self):
        # 当需要pop出堆顶元素时，将其与list的最后一个元素交换，使最后一个元素成为堆顶节点，继而对index为0的节点自上而下一遍即可完成heap调整
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        value = self.nums.pop()
        self.shift_down(0)
        return value


    def shift_up(self):
        # 默认push的时候会append到list的最后一个，所以只需要比较其于父节点的大小即可，当插入节点值比父节点大时，交换必然还是heap；小于则不交换还是heap
        index = len(self.nums) - 1
        # 这个地方的index>=0没有等号的原因在于，当index为1或2时，已经和self.nums[0]对比过了，而索引为1或2的位置正好是self.nums[0]的左右子节点
        while index>0 and self.nums[index] > self.nums[(index-1)//2]:
            self.nums[index], self.nums[(index - 1) // 2] = self.nums[(index-1)//2], self.nums[index]
            index = (index-1)//2


    def shift_down(self, index):

        # 索引越大，越往堆底移动
        while (2*index+1) <= (len(self.nums) - 1):

            # heap中，索引为i的节点，其父节点索引(i-1)//2，其左子节点为2*i+1，右子节点为2*i+2
            left, right = 2*index+1, 2*index+2
            max_index = left

            # 比较左右子节点的值，保存较大的子节点index
            if len(self.nums) > right and self.nums[left] < self.nums[right]:
                max_index = right

            if self.nums[index]<self.nums[max_index]:
                # 当某个子节点大于父节点时(假设为左子节点大于父节点)
                # 1.先交换左子节点与父节点
                # 2.因为交换，左子树可能不再是heap，故需要从左子节点向下调整，所以将max_index赋给index
                self.nums[index], self.nums[max_index] = self.nums[max_index], self.nums[index]
                index = max_index
            else:
                # 当heap的父节点大于左右子节点时，认为heap无需调整 break，其左右子树在上一次循环已经调整到位了
                break

if __name__ == "__main__":
    nums = [1,4,6,7,2,4,6,7,9,100]
    heap = Heap(nums)
    print(heap.nums)

    heap.heapify()
    print(heap.nums)

    heap.push(200)
    print(heap.nums)

    res = []
    while(heap.nums):
        res.insert(0, heap.pop())
    print(heap.nums)
    print(res)