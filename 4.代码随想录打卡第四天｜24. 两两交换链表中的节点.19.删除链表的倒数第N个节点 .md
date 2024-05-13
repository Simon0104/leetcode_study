![Alt text](image-9.png)

1.首先创建虚拟头节点dummyhead，和cur节点负责遍历
2.因为操作该节点的情况，必须是移动至该节点的前一个节点才可以
3.while loop（当cur的下一个和下下个节点都不为NULL时）执行操作
因为读取节点的时候，其实是要链接到数据域，但是因为反转链表需要断开节点，所以需要提前保存两个断开节点的node
4.如上图所示：首先使用temp等于=的头节点，然后temp1=3节点
5.然后开始反转：首先cur指向2node
此时一定要切记该时的链表已经改变，2node指向1node，然后1node指向3
6.完成后要改变cur指针向后移动
7.返回的应该是dummyhead的下一位，即虚拟指针的下一位才为真正头指针也就是链表



ListNode *dummyhead = new ListNode(0);
dummyhead->next = head;
ListNode *cur = dummyhead;
while(cur->next ! = null && cur->next->next != NULL){
    ListNode *temp = cur->next;
    ListNode *temp1 = cur->next->next->next;
    cur->next = cur->next->next;
    cur->next = temp;
    cur->next->next = temp1;
    cur = cur->next->next
}
    ListNode* result = dummyHead->next;
    delete dummyHead;
    return result;


19.删除链表的倒数第N个节点 
![Alt text](image-10.png)

以下为代码：
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummyhead = new ListNode();
        dummyhead->next = head;
        ListNode *fastindex = dummyhead;
        ListNode *slowindex = dummyhead;
        while(n-- && fastindex != NULL){
            fastindex = fastindex->next;
        }
        fastindex = fastindex->next;
//多走一步，这样当fast和slow同时移动的时候，slow才能停在所要删除的index前面
        while(fastindex != NULL){
            fastindex = fastindex->next;
            slowindex = slowindex->next;
        }
        slowindex->next = slowindex->next->next;
    return dummyhead->next;
    }
};

面试题 02.07. 链表相交

Given two (singly) linked lists, determine if the two lists intersect. Return the inter­ secting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.


以下为代码：
// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode(int x) : val(x), next(NULL) {}
//  * };
//  */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *curA = headA;
        ListNode *curB = headB;
        int lenA = 0,lenB = 0;
        while(curA != NULL){
            curA = curA->next;
            lenA++;
        }
        while(curB != NULL){
            curB = curB->next;
            lenB++;
        }
        curA = headA;
        curB = headB;
        if(lenB > lenA){
            swap(lenA,lenB);
            swap(curA,curB);
        } 
        int gap = lenA - lenB;
        while(gap--){
            curA = curA->next;
        }
        while(curA != NULL){
            if(curA == curB){
                return curA;
            }
        curA = curA->next;
        curB = curB->next;
        }
        return NULL;
    }
};