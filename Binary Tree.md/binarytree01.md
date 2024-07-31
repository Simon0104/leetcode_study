
```cpp
struct TreeNode{
    // struct TreeNode defines a structure named TreeNode, which is commonly used to represent a node in a binary tree.
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode(int x) : val(x), left(null), right(null){}
};
```
example how to create a binary tree cpp
```cpp
struct TreeNode{
    int val;
    TreeNode *left;
    Treeode *right;
    TreeNode(int x) : val(x),left(null),right(null){}
};
int main{
    // Creating individual nodes
    TreeNode *root = TreeNode(1);
    TreeNode *left = TreeNode(2);
    TreeNode *right = TreeNode(3);
    // connecting nodes to the root
    root->left = leftChild;
    root->right = rightChild;
    // Printing the tree structure
    cout << "Root value: " << root->val << endl;
    cout << "Left child value: " << root->left->val << endl;
    cout << "Right child value: " << root->right->val << endl;
    
    // Deleting nodes to free memory
    delete root;
    delete leftChild;
    delete rightChild;
    
    return 0;
}
```
py
```py
class TreeNode:
    def _init_(self,val,left = none,right = none):
        self.val = val
        self.left = left
        self.right = right
```
example how to create a binary tree python
```py
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)

    root.left = left_child
    root.right = right_child

    printf("this is th root",root.val)
    printf("this is the left",root.left.val)
    printf("this is the right",root.right.val)
```


144. Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.
![Alt text](image.png)
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
preorder traversal of a binary tree
```cpp
// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//  *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//  *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
//  * };
//  */
// class Solution {
// public:
//     void traversal(TreeNode *cur,vector<int> &vec){
//         if(cur == nullptr){
//             return ;
//         }
//         else{
//             vec.push_back(cur->val);
//             traversal(cur->right,vec);
//             traversal(cur->left,vec);
//         }
//     }
//     vector<int> preorderTraversal(TreeNode* root) {
//         vector <int> result;
//         traversal(root,result);
//         return result;
//     }
// };

class Solution{
public:
    vector<int> preorderTraversal(TreeNode* root){
        vector<int>result;
        stack<TreeNode*> st;
        if(root == NULL){
            return result;
        }
        else{
            st.push(root);
            while(! st.empty()){
                TreeNode* node = st.top();
                st.pop();
                result.push_back(node->val);
                if(node->right){
                    st.push(node->right);
                }
                if(node->left){
                    st.push(node->left);
                }
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        def dfs(node):
            if node is None:
                return
            else:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
                # 其实这里的每一行都是一次dfs从头run到结尾的函数
        dfs(root)
        return result
```