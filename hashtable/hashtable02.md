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
            // 例如:record[2] = 0,左面是键，右边是数值
            // 插入键值对的方法：
            // 1.map[key] = val;
            // 2.map.insert({key,val});
        }
        return {};  // 如果没有找到，返回空的向量
    }
};
```

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i,num in enumerate(nums):
            # 最常用的方法，同时获取索引和元素
        # for i in range(len(nums)):
            # num = nums[i]
            complement = target - nums[i]
            if complement in record:
                return [record[complement],i]
            record[num] = i
        return []
```

15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // 首先设定a
        vector<vector<int>> result;
        sort(nums.begin(),nums.end());
        for(int i = 0;i<nums.size();i++){
            if(nums[i]>0){
                break;
            }
            if(i>0 and nums[i] == nums[i-1]){
                continue;
            }
            unordered_set<int>seen;
            for(int j = i+1;j<nums.size();j++){
                if((j>i+2) and (nums[j] == nums[j-1]) and (nums[j-1] == nums[j-2])){
                    continue;
                }
                int c = 0 - (nums[i] + nums[j]);
                if (seen.find(c) != seen.end()) {
                    result.push_back({nums[i], nums[j], c});
                    seen.erase(c);// 三元组元素c去重
                } else {
                    seen.insert(nums[j]);
                }
            }
        }
        return result;
    }
};
```