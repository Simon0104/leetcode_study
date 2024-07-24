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
        ListNode *dummyhead = new ListNode(0);
        dummyhead->next = head;
        ListNode *cur = dummyhead;
        if(head == nullptr){
            return {};
        }
        while(cur != nullptr and cur->next != nullptr){
            if(cur->next->val == val){
                cur->next = cur->next->next;
            }
            else{
                cur = cur->next;
            } 
        }
        ListNode *result = dummyhead->next;
        delete dummyhead;
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
        dummyhead = ListNode(0)
        dummyhead.next = head
        cur = dummyhead
        if(head == None):
            return None
        while (cur.next != None):
            if(cur.next.val == val):
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyhead.next
```
cuz in remove_elements prob, we just need if-else struct, while we should move the pointer at the previous position of the target val, we can set the dummyhead


1.   Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
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
    ListNode* reverseList(ListNode* head) {
        ListNode *cur = head;
        ListNode *pre = nullptr;
        if(head == nullptr){
            return nullptr;
        }
        while(cur != nullptr){
            ListNode *index = cur->next;
            cur->next = pre;
            pre = cur;
            cur = index;
        }
        return pre;
    }
};
```

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while(cur != None):
            index = cur.next
            cur.next = pre
            pre = cur
            cur = index
        return pre
```

reverse the linked_list, we just nedd to define 3 pointer is fine
In the process of inverse, the head node of the linked list will not change, but the direction of its pointer will be reversed. Therefore, there is no need for additional dummyhead pointer to deal with the boundary situation.


1.  Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

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
    ListNode* swapPairs(ListNode* head) {
        ListNode *dummyhead = new ListNode(0);
        dummyhead->next = head;
        ListNode *cur = dummyhead;
        while(cur->next != nullptr && cur->next->next != nullptr){
            ListNode *temp = cur->next;
            ListNode *temp1 = cur->next->next->next;
            cur->next = cur->next->next;
            cur->next->next = temp;
            cur->next->next->next = temp1;
            cur = cur->next->next;
        }
        ListNode *result = dummyhead->next;
        delete dummyhead;
        return result;
    }
};
```

```py

```


we can't just change the value inside the node, but need to actually exchange nodes.
so that why we should define the dummyhead


19.  Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummyhead = new ListNode(0);
        dummyhead->next = head;
        ListNode *fast = dummyhead;
        ListNode *slow = dummyhead;
        while(n-- and fast != nullptr){
                fast = fast->next;
        }
        fast = fast->next;
        while(fast != nullptr){
            slow = slow->next;
            fast = fast->next;
        }
        slow->next = slow->next->next;
        return dummyhead->next;
    }
};
```

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyhead = ListNode(0,head)
        slow = fast = dummyhead
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummyhead.next
```
Fast first takes n + 1 step, why n+1, because only when moving at the same time can slow point to the previous node of the deleted node (convenient for deletion operations).


2095. Delete the Middle Node of a Linked List
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 
Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode *fast = head;
        ListNode *slow = head;
        ListNode *pre = nullptr;
        if(head->next == nullptr){
            return nullptr;
        }
        while(fast != nullptr && fast->next != nullptr){
            fast = fast->next->next;
            pre = slow;
            slow = slow->next;
        }
        pre->next = pre->next->next;
        return head;
    }
};
```
