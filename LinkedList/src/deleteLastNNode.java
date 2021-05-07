/**
 * @Author lee
 * @Date 2021/5/7 8:41 PM
 **/

import java.util.*;

/*
删除链表倒数第n个节点

采用双指针方法，前面的指针先走n个节点，后面的指针再从头指针开始走，待前面的指针走到链表末尾，便找到要删除的节点
 */

public class deleteLastNNode {
    public static class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }

    }

    /**
     * @param head ListNode类
     * @param n    int整型
     * @return ListNode类
     */
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // write code here
        ListNode font = head;
        while (n-- > 0) {   // font先走n
            font = font.next;
        }
        ListNode behind = head; // behind从头开始
        // 如果font已经为空（走到链表末尾），说明要删除的节点是头结点
        if (font == null) {
            return head.next;
        }
        // 两个指针一起走
        while (font.next != null) {
            font = font.next;
            behind = behind.next;
        }
        // 删除，因为此处是font.next != null 所以我们找到的是要删除节点的pre
        behind.next = behind.next.next;
        return head;
    }
}
