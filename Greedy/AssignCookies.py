# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/2 4:08 下午
@Author:     wz
@File:       AssignCookies.py
@Decs:
"""


'''
question：
有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。
每个孩子只能吃一个饼干，且只有饼干的大小不小于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩子可以吃饱。

example：
输入两个数组，分别代表孩子的饥饿度和饼干的大小。输出最多有多少孩子可以吃饱的数量。
Input: [1,2], [1,2,3]
Output: 2
'''

class Solution():
    def __init__(self, children, cookies):
        self.children, self.cookies = children, cookies


    def find_content_children(self):

        children = sorted(self.children)
        cookies = sorted(self.cookies)

        print("children:", children)
        print("cookies: ", cookies)

        # 这里的贪心体现为：为孩子都只分配最小的满足其饥饿度的cookie，直到cookies或children列表迭代完
        child, cookie = 0, 0
        while (child<len(children) and cookie<len(cookies)) :
            if cookies[cookie]>=children[child]:
                child += 1
            cookie += 1
        return child



if __name__ == "__main__":
    children = [1,4,6,7,2,4,6,7,9,100]
    cookies = [1,3,2,5,6,4,10]

    solution = Solution(children, cookies)
    print(solution.find_content_children())
