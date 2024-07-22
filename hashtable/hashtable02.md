1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        int index = 0; 
        for (auto i : nums) {
            if (map.find(target - i) != map.end()) {
                return {map[target - i], index};
            }
            map[i] = index;
            index++;
        }
        return {};
    }
};
```

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> record;  // 初始化一个空的哈希表
        for (int i = 0; i < nums.size(); i++) {  // 遍历数组
            int complement = target - nums[i];  // 计算补数
            if (record.find(complement) != record.end()) {  // 如果补数在哈希表中
                return {record[complement], i};  // 返回补数的索引和当前元素的索引
            }
            record[nums[i]] = i;  // 将当前元素及其索引插入哈希表
            // 例如:record[2] = 0,左面是数值，右边是键
        }
        return {};  // 如果没有找到，返回空的向量
    }
};
```