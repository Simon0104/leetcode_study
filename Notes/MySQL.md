问：为什么mysql使用b+tree，而不是其他二叉树或者hashtable？
答：
1.b+tree只在叶子节点存储数据，所以书的高度更低检索速度也更快，算法复杂度为logn
2.可以使用范围索引：SELECT * WHERE age BETWEEN 10 AND 20
3.每个节点可以存储多个关键字，结构更紧凑所以可以存储更多关键字