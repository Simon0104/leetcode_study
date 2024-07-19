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
        int record[26] = {0};
        for(int i = 0;i < s.size();i++){
            record[s[i] - 'a']++;
        }
        for(int j = 0;j < t.size();j++){
            record[t[j] - 'a']--;
        }
        for(int a = 0;a < 26;a++){
            if(record[a] != 0){
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
        record = [0] * 26
        for i in s:
            record[ord(i) - ord("a")]+=1
            # In Python, the ord function is used to get the ASCII value of a character
        for j in t:
            record[ord(j) - ord("a")]-=1
        for a in range(26):
            if(record[a] != 0):
                return False
        return True
```
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