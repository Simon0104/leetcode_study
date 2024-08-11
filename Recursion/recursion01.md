77. Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

```cpp
class Solution {
private:
    vector<vector<int>> result; // 存放符合条件结果的集合
    vector<int> path; // 用来存放符合条件结果
    void backtracking(int n, int k, int startIndex) {
        for (int i = startIndex; i <= n; i++) {
            path.push_back(i); // 处理节点
            backtracking(n, k, i + 1); // 递归
            path.pop_back(); // 回溯，撤销处理的节点
        }
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        backtracking(n, k, 1);
        return result;
    }
};

path = [1]

backtracking(n, k, 1+1=2); // 递归
此时startindex=2

if为false不执行

i = startindex = 2
path.push_back(i)
path = [1,2]

backtracking(n, k, 2+1=3); // 递归
此时i=2，startindex=3

result = [[1,2]]
return回到backtracking(n, k, 2+1=3); // 递归
然后path.pop_back()  得到path = [1]
此时结束了一次for loop，所以i++

此时i=2重新进入for loop，push进入path = [1,3].....

以此往复直到当i=5>4，不再符合for loop条件的时候，
再次返回上一次recursive的位置(第一次进入的时候) path = [],i = 1，然后i++

gpt：
当 i = 5 时的执行步骤
检查 for 循环条件：

代码：for (int i = startIndex; i <= n; i++)
当前状态：startIndex = 5，n = 4。
解释：此时 i = 5，因为 i > n，for 循环条件不再满足，所以 for 循环将不再执行，程序跳到循环之后的代码。
退出 for 循环：

操作：for 循环结束，当前递归函数中的所有代码已执行完毕。
解释：由于没有更多的循环内容可以执行，程序退出当前递归函数。
返回到上一层递归：

返回位置：程序会返回到调用当前递归函数的地方。这通常是上一层递归函数中的 backtracking(n, k, startIndex) 语句之后的位置。
执行 path.pop_back();：
代码：path.pop_back();
解释：撤销当前路径的最后一个选择。假设当前 path 是 [1, 4]，执行 path.pop_back(); 后，path 变为 [1]。
继续 for 循环：
在上一层递归的 for 循环中，i 的值会递增，i++。
上一层递归的 for 循环继续：

执行 i++：i 在上一层递归的 for 循环中递增。例如，如果上一层 for 循环当前处理的是 i = 4，此时 i 将递增为 5。
再次检查 for 循环条件：
如果 i = 5 在上一层递归中，for 循环同样会结束，程序返回到更上一层递归。
逐层返回，直到最外层：

如果 for 循环中的 i 在所有递归层次上都已经超过 n，那么程序最终会回到最外层的递归调用。
这个过程会重复，直到所有递归层次都退出并返回到 combine 函数。
总结
当 i = 5 时，for 循环条件不再满足，程序退出当前递归函数，返回到上一层递归。
返回上一层后，path.pop_back() 撤销上一步选择，然后 for 循环中的 i++ 执行，检查是否继续循环或返回更上一层递归。
最终，程序会逐层返回，直到所有递归层次都结束，完成组合的生成。
```
```py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = list()
        path = list()
        self.backtracking(n, k, 1, path, result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n + 1):
            path.append(i)  
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  
```

216. Combination Sum III
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

```cpp
class Solution {
private:
    vector<vector<int>>result;
    vector<int>path;
    void backstracking(int k,int n,int sum,int startindex){
        if(path.size() == k and sum == n){
            result.push_back(path);
            return;
        }
        for(int i = startindex;i<=9;i++){
            path.push_back(i);
            sum += i;
            backstracking(k,n,sum,i+1);
            sum -= i;
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        backstracking(k,n,0,1);
        return result;
    }
};
```

```py
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = list()
        path = list()
        sum = 0
        self.backstracking(k,n,1,result,path,sum)
        return result
    def backstracking(self,k,n,start,result,path,sum):
        if len(path) == k and sum == n:
            result.append(path[:])
#      为什么使用 path[:] 而不是直接 result.append(path)？
# 如果直接使用 result.append(path)，那么 result 中保存的每个元素实际上都是同一个 path 列表的引用。当 path 列表在递归过程中发生变化时，result 中保存的所有 path 都会跟着变化，这不是我们想要的。

# 通过使用 path[:]，我们确保每次添加到 result 中的都是当前 path 的一个独立副本，这样即使 path 后续发生变化，result 中已保存的组合不会受到影响。

# 例子：
# python
# Copy code
# path = [1, 2, 3]
# result = []
# result.append(path[:])  # 添加 path 的拷贝
# path.append(4)          # 修改 path
# print(result)  # 输出 [[1, 2, 3]]，即使 path 改变了，result 中的内容不受影响
# 如果你在编写代码时需要保存当前状态（比如当前组合 path），并且后续还可能修改 path，就需要使用 path[:] 来保存一个副本。
            return
        for i in range(start,10):
            path.append(i)
            sum += i
            self.backstracking(k,n,i+1,result,path,sum)
            sum -= i
            path.pop()
            
```


216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [ [1,2,6],[1,3,5],[2,3,4] ]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

```cpp
class Solution {
private:
    vector<vector<int>>result;
    vector<int>path;
    void backstracking(int k,int n,int sum,int startindex){
        if(path.size() == k and sum == n){
            result.push_back(path);
            return;
        }
        for(int i = startindex;i<=9;i++){
            path.push_back(i);
            sum += i;
            backstracking(k,n,sum,i+1);
            sum -= i;
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        backstracking(k,n,0,1);
        return result;
    }
};
```