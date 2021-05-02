/**
 * @Author lee
 * @Date 2021/4/30 11:12 AM
 * <p>
 * 牛客NC93--设计LRU缓存结构
 * **********************
 * 题目描述
 * **********************
 * 设计LRU缓存结构，该结构在构造时确定大小，假设大小为K，并有如下两个功能
 * set(key, value)：将记录(key, value)插入该结构
 * get(key)：返回key对应的value值
 * [要求]
 * set和get方法的时间复杂度为O(1)
 * 某个key的set或get操作一旦发生，认为这个key的记录成了最常使用的。
 * 当缓存的大小超过K时，移除最不经常使用的记录，即set或get最久远的。
 * 若opt=1，接下来两个整数x, y，表示set(x, y)
 * 若opt=2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回-1
 * 对于每个操作2，输出一个答案
 * **********************
 * 样例
 * **********************
 * 输入：[[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
 * 输出：[1,-1]
 * **********************
 * 思路
 * **********************
 * 用到的数据结构：双向链表、HashMap
 * 哈希查，查的快；链表删，删的快
 * 对于LRU缓存结构双向链表，操作包括：put(插入数据)、get(获取数据)
 * LRU的每次操作(get,put)都会将节点放入链表首部
 * 涉及底层操作：
 * deleteNode，删除：删除某个节点
 * addToHead，插入到表头：LRU有足够的空间，新插入的元素直接放在表头
 * moveToHead，移动到表头：使用过某条数据后，需要将其移动到表头。由deleteNode和addToHead完成
 * removeLast，删除最后一个元素：链表结构超过固定size，删除最后元素。有返回值，用于map的维护
 * 用HashMap 来存(key, DoubleLinkedNode)，便于获取node.val
 */

/**
 * 牛客NC93--设计LRU缓存结构 LeetCode--LRU缓存机制（146）
 * **********************
 * 题目描述
 * **********************
 * 设计LRU缓存结构，该结构在构造时确定大小，假设大小为K，并有如下两个功能
 * set(key, value)：将记录(key, value)插入该结构
 * get(key)：返回key对应的value值
 * [要求]
 * set和get方法的时间复杂度为O(1)
 * 某个key的set或get操作一旦发生，认为这个key的记录成了最常使用的。
 * 当缓存的大小超过K时，移除最不经常使用的记录，即set或get最久远的。
 * 若opt=1，接下来两个整数x, y，表示set(x, y)
 * 若opt=2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回-1
 * 对于每个操作2，输出一个答案
 * **********************
 * 样例
 * **********************
 * 输入：[[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
 * 输出：[1,-1]
 * **********************
 * 思路
 * **********************
 * 用到的数据结构：双向链表、HashMap
 * 哈希查，查的快；链表删，删的快
 * 对于LRU缓存结构双向链表，操作包括：put(插入数据)、get(获取数据)
 * LRU的每次操作(get,put)都会将节点放入链表首部
 * 涉及底层操作：
 * deleteNode，删除：删除某个节点
 * addToHead，插入到表头：LRU有足够的空间，新插入的元素直接放在表头
 * moveToHead，移动到表头：使用过某条数据后，需要将其移动到表头。由deleteNode和addToHead完成
 * removeLast，删除最后一个元素：链表结构超过固定size，删除最后元素。有返回值，用于map的维护
 * 用HashMap 来存(key, DoubleLinkedNode)，便于获取node.val
 *  **********************
 *  应用
 *  **********************
 *  偏向内存管理
 *  MySQL的buffer pool 冷热端数据维护，页面置换
 *  Redis 的一种内存淘汰策略
 */


import java.util.*;


class LRUCache {
    // 自定义双向链表
    static class DoubleLinkedNode {
        int key, val;
        DoubleLinkedNode prev, next;

        public DoubleLinkedNode(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    DoubleLinkedNode dummyHead, dummyTail;
    Map<Integer, DoubleLinkedNode> map;
    int size, capacity;

    // 构造函数，初始化
    public LRUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>();
        dummyHead = new DoubleLinkedNode(-1, -1);
        dummyTail = new DoubleLinkedNode(-1, -1);
        dummyHead.next = dummyTail;
        dummyTail.prev = dummyHead;
        size = 0;
    }

    // 维护两个指针
    private void deleteNode(DoubleLinkedNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    // 维护4个指针
    private void addToHead(DoubleLinkedNode node) {
        node.next = dummyHead.next;
        node.prev = dummyHead;

        dummyHead.next.prev = node;
        dummyHead.next = node;
    }

    // 维护6个指针，这种设计就很好
    private void moveToHead(DoubleLinkedNode node) {
        deleteNode(node);
        addToHead(node);
    }

    private DoubleLinkedNode removeLast() {
        DoubleLinkedNode lastNode = dummyTail.prev;
        deleteNode(lastNode);
        return lastNode;
    }

    public int get(int key) {
        DoubleLinkedNode node = map.get(key);
        if (node == null) {
            return -1;
        }
        // get后移动到表头
        moveToHead(node);
        return node.val;
    }

    public void put(int key, int val) {
        //put操作有则更新；无则创建，超过长度时，需要同时删除链表和map中的数据
        DoubleLinkedNode node = map.get(key);
        if (node != null) {//有，更新
            node.val = val;
            moveToHead(node);
        } else {//无，创建
            node = new DoubleLinkedNode(key, val);
            map.put(key, node);
            addToHead(node);
            size++;
            if (size > capacity) {// 超长，删数据
                DoubleLinkedNode tail = removeLast();
                map.remove(tail.key);
                size--;
            }
        }
    }
}


public class LRU {
    /**
     * lru design
     * @param operators int整型二维数组 the ops
     * @param k int整型 the k
     * @return int整型一维数组
     */
    public int[] Solution(int[][] operators, int k) {
        LRUCache cache = new LRUCache(k);
        ArrayList<Integer> record = new ArrayList<>();
        for (int[] item : operators) {
            int operation = item[0];
            if (operation == 1) {
                cache.put(item[1], item[2]);
            } else {
                record.add(cache.get(item[1]));
            }
        }
        int length = record.size();
        int[] res = new int[length];
        for (int i = 0; i < length; i++) {
            res[i] = record.get(i);
        }
        for (int r:res){
            System.out.println(r);
        }
        return res;

    }

    // 输入：[[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
    // 输出：[1,-1]

    public static void main(String[] args) {

        ArrayList<ArrayList<Integer>> example = new ArrayList<>();
        example.add(new ArrayList<>(Arrays.asList(1, 1, 1)));
        example.add(new ArrayList<>(Arrays.asList(1, 2, 2)));
        example.add(new ArrayList<>(Arrays.asList(1, 3, 2)));
        example.add(new ArrayList<>(Arrays.asList(2, 1)));
        example.add(new ArrayList<>(Arrays.asList(1, 4, 4)));
        example.add(new ArrayList<>(Arrays.asList(2, 2)));
        int lru_size = 3;

        int length = example.size();
        int [][] in = new int[length][3];
        for(int i = 0; i< length; i++){
            if (example.get(i).get(0) == 1) {
                for (int j = 0; j < 3; j++) {
                    in[i][j] = example.get(i).get(j);
                }
            }else{
                for (int j = 0; j < 2; j++) {
                    in[i][j] = example.get(i).get(j);
                    }
                }
        }

        LRU lru = new LRU();
        lru.Solution(in, lru_size);

    }
}
