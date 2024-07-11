203. Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
```cpp
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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode *cur = dummyHead;
        while(cur->next != nullptr){
            if(cur->next->val == val){
                ListNode *tep = cur->next;
                cur->next = cur->next->next;
                delete tep;
            }
            else{
                cur = cur->next;
            }
        }
        ListNode * result = dummyHead->next;
        delete dummyHead;
        return result;
    }
};
```
ListNode *tep = cur->next;

To avoid memory leaks: When you bypass a node in a linked list, the node being bypassed is no longer accessible through any pointer in the list. If you don't store a pointer to it before bypassing it, you won't be able to deallocate its memory, leading to a memory leak.

To safely update pointers: When you update the next pointer of the current node to skip over the node that is to be removed, you need to have a reference to the node that is being removed so you can properly deallocate its memory.

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyhead = ListNode(next = head)
        cur = dummyhead
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyhead.next
```