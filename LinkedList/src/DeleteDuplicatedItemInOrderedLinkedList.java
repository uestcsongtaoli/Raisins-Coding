/**
 * @Author lee
 * @Date 2021/5/12 9:53 AM
 * 给出一个升序排序的链表，删除链表中的所有重复出现的元素，只保留原链表中只出现一次的元素。
 * *************
 * 朴素解法 deleteDuplicates1
 * *************
 * 用一个map来存里面的元素，选择不重复的，排序（保证顺序）；重新构建链表
 * *************
 * 双指针 deleteDuplicates2
 * *************
 * 双指针+dummyHead：前后两个指针，找到重复的，就继续找，找出所有的重复值，断链，继续。
 **/

import java.util.*;

public class DeleteDuplicatedItemInOrderedLinkedList {
    public static class ListNode {
        int val;
        ListNode next = null;

        public ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode deleteDuplicates1(ListNode head) {
        // write code here
        Map<Integer, Integer> map = new HashMap<>(); // 存val的映射
        ArrayList<Integer> res = new ArrayList<>(); // 不重复的元素
        ListNode curr = head;
        // 统计链表中的元素，counter
        while (curr != null) {
            if (map.containsKey(curr.val)) {
                map.put(curr.val, map.get(curr.val) + 1);
            } else {
                map.put(curr.val, 1);
            }
            curr = curr.next;
        }
        // keySet() 方法返回映射中所有 key 组成的 Set 视图。
        // keySet() 方法可以与 for-each 循环一起使用，用来遍历迭代 HashMap 中的所有键
        for (int i : map.keySet()) {
            if (map.get(i) == 1) {
                res.add(i);
            }
        }
        int i = 0;
        ListNode dummyHead = new ListNode(0);
        ListNode p = dummyHead;
        // 排序
        Collections.sort(res);
        // 重新构建列表
        while (i < res.size()) {
            ListNode node = new ListNode(res.get(i));
            p.next = node;
            p = node;
            i++;
        }
        return dummyHead.next;
    }

    public ListNode deleteDuplicates2(ListNode head) {
        // dummyHead 有利于返回
        ListNode dummyHead = new ListNode(-1);
        dummyHead.next = head;
        // 前后指针
        ListNode front = head;
        ListNode behind = dummyHead;
        // 因为循环里面用到了 front.next
        while (front != null && front.next != null) {
            // 后一个节点的值等于前一个节点
            if (front.val == front.next.val) {
                ListNode temp = front.next;
                // 找到所有相等的节点
                while (temp != null && temp.val == front.val) {
                    temp = temp.next;
                }
                // temp为下一个不相等的节点 1，2，2，2，3，此时temp在3
                front = temp;
                // 断链，删除
                behind.next = temp;
            } else {
                front = front.next;
                behind = behind.next;
            }
        }
        return dummyHead.next;
    }


}