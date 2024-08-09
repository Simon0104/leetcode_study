515. Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        vector<int>result;
        queue<TreeNode*>que;
        if(root == NULL){
            return result;
        }
        else{
            que.push(root);
            while(!que.empty()){
                int length = que.size();
                vector<int>vec;
                for(int i = 0;i<length;i++){
                    TreeNode* node = que.front();
                    que.pop();
                    vec.push_back(node->val);
                    if(node->left){
                        que.push(node->left);
                    }
                    if(node->right){
                        que.push(node->right);
                    }
                }
                sort(vec.begin(),vec.end());
                result.push_back(vec.back());
            }
        }
        return result;
    }
};
```

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        queue = deque()
        if(root is None):
            return result
        else:
            queue.append(root)
            while(queue):
                length = len(queue)
                vector = list()
                for i in range(length):
                    cur = queue.popleft()
                    vector.append(cur.val)
                    if(cur.left):
                        queue.append(cur.left)
                    if(cur.right):
                        queue.append(cur.right)
                max_value = max(vector)
                result.append(max_value)
        return result
```

116. Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []

一开始就是有tree的
key!!!!
first loop
```cpp
queue<Node*> que;
if (root != NULL) que.push(root);
que = [1]
while (!que.empty()) {
    int size = que.size();  // size = 1
    Node* nodePre = nullptr;
    Node* node = nullptr;
    for (int i = 0; i < size; i++) {
        node = que.front(); // node = 1
        que.pop();
        if (i == 0) {
            nodePre = node; // nodePre = 1
        } else {
            nodePre->next = node;
            nodePre = nodePre->next;
        }
        if (node->left) que.push(node->left);   // que = [2]
        if (node->right) que.push(node->right); // que = [2, 3]
    }
    nodePre->next = NULL;
}

       1 -> NULL
     /   \
    2     3
   / \   / \
  4   5 6   7

que = [2, 3]
```
second loop
```cpp
while (!que.empty()) {
    int size = que.size();  // size = 2
    Node* nodePre = nullptr;
    Node* node = nullptr;
    for (int i = 0; i < size; i++) {
        node = que.front(); // node = 2, then node = 3
        que.pop();
        if (i == 0) {
            nodePre = node; // nodePre = 2
        } else {
            nodePre->next = node; // 2 -> 3
            nodePre = nodePre->next; // nodePre = 3
        }
        if (node->left) que.push(node->left);   // que = [4], then que = [4, 5]
        if (node->right) que.push(node->right); // que = [4, 5, 6], then que = [4, 5, 6, 7]
    }
    nodePre->next = NULL; // 3 -> NULL
}
       1 -> NULL
     /   \
    2  -> 3 -> NULL
   / \   / \
  4   5 6   7
que = [4, 5, 6, 7]

```
third loop
```cpp
while (!que.empty()) {
    int size = que.size();  // size = 4
    Node* nodePre = nullptr;
    Node* node = nullptr;
    for (int i = 0; i < size; i++) {
        node = que.front(); // node = 4, then node = 5, then node = 6, then node = 7
        que.pop();
        if (i == 0) {
            nodePre = node; // nodePre = 4
        } else {
            nodePre->next = node; // 4 -> 5, then 5 -> 6, then 6 -> 7
            nodePre = nodePre->next; // nodePre = 5, then nodePre = 6, then nodePre = 7
        }
        if (node->left) que.push(node->left);   // no children, queue unchanged
        if (node->right) que.push(node->right); // no children, queue unchanged
    }
    nodePre->next = NULL; // 7 -> NULL
}
       1 -> NULL
     /   \
    2  -> 3 -> NULL
   / \   / \
  4-> 5->6 ->7 -> NULL
que = []

```

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        queue<Node*>que;
        if(root == NULL){
            return 0;
        }
        que.push(root);
        while(! que.empty()){
            int length = que.size();
            Node* nodepre = nullptr;
            Node* node = nullptr;
            for(int i = 0;i<length;i++){
                if(i == 0){
                    nodepre = que.front();
                    que.pop();
                    node = nodepre;
                }
                else{
                    node = que.front();
                    que.pop();
                    nodepre->next = node;
                    nodepre = nodepre->next;
                }
                if(node->left){
                    que.push(node->left);
                }
                if(node->right){
                    que.push(node->right);
                }
            }
            // 当一层loop结束的时候，将最后一个指向null
            nodepre->next = NULL;
        }
        return root;
    }
};
```
```py
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        if(not root):
            return None
        queue.append(root)
        while(queue):
            length = len(queue)
            node = None
            nodepre = None
            for i in range(length):
                if(i == 0):
                    nodepre = queue.popleft()
                    node = nodepre
                else:
                    node = queue.popleft()
                    nodepre.next = node
                    nodepre = nodepre.next
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            nodepre.next = None
        return root


```


keynote
```cpp
在C++中，判断一个变量是存储值的变量还是存储指向节点的引用（指针）的关键在于变量的定义和使用。下面是一些指导原则，可以帮助你区分这两种情况：

### 存储值的变量
1. **定义**：存储值的变量直接存储实际的数据，如整数、浮点数或结构体等。
2. **使用**：存储值的变量在使用时直接访问或修改数据。

```cpp
int a = 5;        // a 是存储整数值的变量
float b = 3.14;   // b 是存储浮点数值的变量
Node node;        // node 是存储 Node 结构体的变量
node.val = 10;    // 直接访问 node 的成员
```

### 存储指向节点的引用（指针）
1. **定义**：存储指向节点的引用（指针）变量存储的是数据的内存地址，用于指向某个对象或节点。
2. **使用**：指针变量在使用时需要通过解引用（使用`*`操作符）来访问或修改指针指向的对象。

```cpp
Node* nodePtr = new Node();  // nodePtr 是存储指向 Node 对象的指针
nodePtr->val = 10;           // 通过指针访问和修改 Node 对象的成员
```

### 示例解释

假设我们有一个 `Node` 结构体定义如下：

```cpp
struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

#### 存储值的变量

```cpp
Node node(1);   // node 是存储值的变量，包含实际的 Node 数据
node.val = 2;   // 直接修改 node 的 val 值
```

#### 存储指向节点的引用（指针）

```cpp
Node* nodePtr = new Node(1);  // nodePtr 是存储指向 Node 对象的指针
nodePtr->val = 2;             // 通过指针修改 Node 对象的 val 值
```

### 判断方法

1. **查看定义**：
   - 如果变量前面有`*`符号（例如`Node*`），它是一个指针，存储的是指向节点的引用。
   - 如果变量没有`*`符号，它是一个值变量，存储的是实际的数据。

2. **查看使用方式**：
   - 如果变量通过`.`操作符来访问成员（例如`node.val`），它是一个值变量。
   - 如果变量通过`->`操作符来访问成员（例如`nodePtr->val`），它是一个指针。

### 例子

以下是一些例子来帮助你理解：

#### 存储值的变量

```cpp
Node node1(1);   // node1 是存储值的变量
Node node2(2);   // node2 是存储值的变量

node1.left = &node2;  // 将 node2 的地址赋值给 node1 的 left 指针
```

#### 存储指向节点的引用（指针）

```cpp
Node* nodePtr1 = new Node(1);  // nodePtr1 是存储指向 Node 对象的指针
Node* nodePtr2 = new Node(2);  // nodePtr2 是存储指向 Node 对象的指针

nodePtr1->left = nodePtr2;     // 通过指针将 nodePtr2 指向的节点赋值给 nodePtr1 的 left 指针
```

### 小结

- 存储值的变量直接包含实际的数据。
- 存储指向节点的引用（指针）包含的是对象的内存地址。
- 定义中使用`*`表示指针，使用`.`操作符访问值变量成员，使用`->`操作符访问指针指向的对象成员。

通过理解变量的定义和使用方式，你可以清楚地区分存储值的变量和存储指向节点的引用（指针）。
```