当我们遇到了要快速判断一个元素是否出现集合里的时候，就要考虑哈希法。但是哈希法也是牺牲了空间换取了时间，因为我们要使用额外的数组，set或者是map来存放数据，才能实现快速的查找

242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int,int> result;
        // 因为是map所以需要键值对，因此需要<int,int>
        for(int i = 0;i<s.size();i++){
            int s_key = s[i] - 'a';
            result[s_key]++; 
        }
        for(int j = 0;j<t.size();j++){
            int t_key = t[j] - 'a';
            result[t_key]--;
        }
        for(int a = 0;a<26;a++){
            if(result[a] != 0){
                return false;
            }
        }
        return true;
    }
};
```

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0]*26
        for i in s:
            result_s = ord(i) - ord("a")
            record[result_s] +=1
        for j in t:
            result_t = ord(j) - ord("a")
            record[result_t] -=1
        for a in range(26):
            if(record[a] != 0):
                return False
        return True
```
conclusion:
查找元素是否匹配可以考虑使用hash，数组就是最简单的hashtable
首先创建一个空的数组vector<int>record(26,0)名字为record都container容器，容量为26位然后初始化为0，这个存储的结果
首先遍历s，求出与‘a’相对位置，讲相对位置保存在上述container，然后遍历t将每一项与container中的相对位置进行比较，最后如果container中存在非零项则return false

Here's what record[ord(i) - ord('a')] += 1 does:

ord(i) gets the ASCII value of the character i.
ord('a') gets the ASCII value of the character 'a' (which is 97).
ord(i) - ord('a') calculates the zero-based index for the character i relative to 'a'. For example, for 'b', it calculates 98 - 97 = 1.
record[ord(i) - ord('a')] accesses the array record at the position corresponding to the character i.
+= 1 increments the count of the character i in the record array.


383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int record[26] = {0};
        if(magazine.size() < ransomNote.size()){
            return false;
        }
        for(int i = 0;i<magazine.size();i++){
            record[magazine[i] - 'a']++;
        }
        for(int j = 0;j<ransomNote.size();j++){
            record[ransomNote[j] - 'a']--;
            if(record[ransomNote[j] - 'a'] < 0){
            return false;
            }
        }
        return true;
    }
};
```

```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        for j in magazine:
            record[ord(j) - ord("a")]+=1
        for i in ransomNote:
            record[ord(i) - ord("a")]-=1
            if record[ord(i) - ord("a")] < 0:
                return False
        return True
```

49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        if(strs.size() == 0){
            return {};
        }
        unordered_map<string,vector<string>> record;
        for(auto i : strs){
            string key = i;
            sort(key.begin(),key.end());
            record[key].push_back(i);
            // Look for the key "aet" in the record. If it does not exist, create a new key-value pair. The value is an empty vector.
            // record["ant"].push_back("tan")
            //             {
            //     "aet": ["eat", "tea"],
            //     "ant": ["tan"]
            // }

        }
        vector<vector<string>>result;
        for(auto i : record){
            result.push_back(i.second);
//      i.first is a key, that is, the sorted string.
//      i.second is a value, that is, a vector containing ectopic words.
        }
        return result;
    }
};
```

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = defaultdict(list)
        for s in strs:
            key = " ".join(sorted(s))
            record[key].append(s)
        return list(record.values())

```
 

 349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> result_set;
        unordered_set<int> nums_set(nums1.begin(),nums1.end());
        for(auto i :nums2){
            if(nums_set.find(i) != nums_set.end()){
                result_set.insert(i);
            }
        }
        return vector<int>(result_set.begin(),result_set.end());
    }
};
```

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_set = set(nums1)
        result_set = set()
        
        for i in nums2:
            if i in nums_set:
                result_set.add(i)
        
        return list(result_set)
```


202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

```cpp
class Solution {
public:
    int get_num(int n){
        int sum = 0;
        while(n != 0){
            int digit = n % 10;
            sum += digit * digit;
            n = n/10;
        }
        return sum;
    }
    bool isHappy(int n) {
        unordered_set<int> result;
        while(result.find(n) == result.end()){
            result.insert(n);
            n = get_num(n);
        }
        for(auto i : result){
            if(i == 1){
                return true;
            }
        }
        return false;
    }
};
```

