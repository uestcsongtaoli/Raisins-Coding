# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/3 4:01 下午
@Author:     wz
@File:       CanPlaceFlowers.py
@Decs:
"""

'''
question：
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
'''


class Solution():
    def __init__(self, flowerbed):
        self.flowerbed =  flowerbed


    def can_place_flowers(self, n):

        flowerbed = [0] + self.flowerbed + [0]
        count = 0
        # 遍历过去就行，注意数组边界即可
        for i in range(1, len(flowerbed)-1): # 很简单，贪心体现在每个地方都想种上花
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                count += 1
                flowerbed[i] = 1

        return count>=n



if __name__ == "__main__":
    flowerbed = [1,0,1,0,0,0,0,1,1]

    solution = Solution(flowerbed)
    print(solution.can_place_flowers(2))
