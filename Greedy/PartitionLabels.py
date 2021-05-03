# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/3 5:06 下午
@Author:     wz
@File:       PartitionLabels.py
@Decs:
"""



'''
question:
给定一个小写字符串S，将其尽可能多地分隔成多个子串，要求每个字母都只出现在一个子串中，依次返回每个子串的长度。

Example:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
'''

class Solution():
    def __init__(self, s):
        self.s =  s


    def partition_labels(self):

        s = self.s
        sub_s = []

        # 先纪录每个字符串最后出现的位置索引，即对于单个字符最断的符合要求子串终止位置
        s_dict = {}
        for i in range(len(s)):
            s_dict[s[i]] = i
        print(s_dict)

        # 思路是用滑窗划出子串的区域，如ababcbacadefegdehijhklij串，s_dict中其a:8,b:5,c:7，
        # 当遍历至ababcb时，b虽到已经终止，但是此时max(a:8,b:5,c:7)=8，故仍然继续遍历
        start, end = 0, 0

        for i in range(len(s)):
            end = max(s_dict[s[i]], end) #贪心在 max取下标i及i前的所有字符的最大值，一次性划了一个大窗口
            if i == end: # 只有当前索引等于大窗口的结束索引时，子串结束
                sub_s.append(i - start + 1) # 纪录子串当前长度
                start, end = i + 1, i + 1 #初始化子串开始位置和结束位置 (起始end位置不需要初始化，在循环中必然会被更新，为保证一致性)

        return sub_s


    """
    note：
    其实质上是s_dict维护了一个区间，对一个字符串，维护了一个[[字母第一次出现的索引，字母最后一次出现的索引], ...]，然后对区间进行合并，又回到区间操作的老问题了
    即，故有以下解法，思路一样，抽象为区间问题，先排序再贪心。
    """
    def partition_labels_intervals(self):

        s = self.s
        sub_s = []

        s_dict = {}
        for i in range(len(s)):
            try:
                s_dict[s[i]] = [s_dict[s[i]][0], i]
            except:
                s_dict[s[i]] = [i, i]
        print(s_dict)

        # char_list按区间开始位置升序排序
        # 这里的区间合并和射气球的区间合并有所不同，射气球要求被合并的区间两两之间都有交集才进行合并，这里是按照被合并区间任意两个有交集就可以合并

        """
        note:
        对区间的开始或终止排序后再操作，是有所不同的，各种不同，请多做习题体会。
        """
        char_list = sorted(s_dict.values(), key=lambda x:x[0])
        print(char_list)

        end = char_list[0][1]
        for char in char_list:
            if char[0] > end:
                sub_s.append(char[0])
                end = char[1]
            else:
                end = max(end, char[1]) # 被合并区间任意两个有交集就可以合并，所以有取max这一操作，每次在合并后，验证是否需要延长结束区间长度

        sub_s = [0] + sub_s + [len(s)]
        res = []
        for i in range(len(sub_s)-1):
            res.append(sub_s[i+1] - sub_s[i])

        return res


if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"

    solution = Solution(s)
    print(solution.partition_labels_intervals())