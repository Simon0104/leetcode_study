![Alt text](image.png)
二叉树可以链式存储，也可以顺序存储。
链式存储方式就用指针
![Alt text](image-1.png)

顺序存储的方式就是用数组。
![Alt text](image-2.png)
就是顺序存储的元素在内存是连续分布的，而链式存储则是通过指针把分布在各个地址的节点串联一起。

cpp中map，set，mutimap和multiset的底层实现都是平衡二叉搜索树，所以map和set的增删操作的timecomplity都是log(n)

二叉树的遍历方式：dfs和bfs 
其中dfs包括前序遍历（中左右）
          中序遍历（左中右）
          后序遍历（左右中）
          ![Alt text](image-3.png)

链式二叉树的定义：
其实是定义一种structure
struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x):val(x),left(NULL),right(NULL){}
};




