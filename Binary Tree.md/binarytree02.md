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
