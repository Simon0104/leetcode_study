344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0;
        int right = s.size()-1;
        while(left<right){
            swap(s[left],s[right]);
            left++;
            right--;
        }
    }
};
```

```py
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        """
        Do not return anything, modify s in-place instead.
        """
```


541. Reverse String II
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

```cpp
class Solution {
public:
    string reverseStr(string s, int k) {
        if(s.size()<k){
            reverse(s.begin(),s.end());
        }
        int n = 2*k;
        if(s.size()>=k and s.size()<n){
            reverse(s.begin(),s.begin()+k);
        }
        if(s.size()>=n){
            for(int i = 0;i<s.size();i+=n){
                if(s.size()>i+k){
                    reverse(s.begin()+i,s.begin()+i+k);
                }
                else{
                    reverse(s.begin()+i,s.end());
                }
            }
        }
        return s;
    }
};
```

```py
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # 将字符串转换为列表以便于修改
        n = 2 * k
        for i in range(0, len(s), n):
            if i + k <= len(s):
                s[i:i + k] = reversed(s[i:i + k])
            else:
                s[i:] = reversed(s[i:])
        return ''.join(s)
```

```py
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Two pointers. Another is inside the loop.
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s
```


151. Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

```cpp
class Solution {
public:
    string reverseWords(string s) {
        removeExtraSpaces(s);
        reverse(s.begin(), s.end());
        int start = 0;
        for (int end = 0; end <= s.size(); end++) {
            if (end == s.size() or s[end] == ' ') {
                reverse(s.begin() + start, s.begin() + end);
                start = end + 1;
            }
        }
        return s;
    }

private:
    void removeExtraSpaces(string& s) {
    // 因为主函数直接引用string，所以无需返回任何数值
    // slow和fast遍历的都是字母并非单词！！！
        int slow = 0;
        for (int fast = 0; fast < s.size(); ++fast) {
            if (s[fast] != ' ') {
                // " "  这个表示字符串
                // ' ' 这个表示字符
                if (slow != 0) s[slow++] = ' ';
                while (fast < s.size() && s[fast] != ' ') {
                    // 此处应该让指针在单词内部遍历了！
                    s[slow++] = s[fast++];
                }
            }
        }
        s.resize(slow);
    }
};
```

```py
class Solution:
    def removeExtraSpaces(self, s: str) -> str:
        # 移除多余空格
        words = s.split()
        return ' '.join(words)

    def reverseWords(self, s: str) -> str:
        # 去除多余空格
        s = self.removeExtraSpaces(s)
        # 反转整个字符串
        s = s[::-1]
        # 将反转后的字符串分割成单词列表
        words = s.split(' ')
        # 反转每个单词
        words = [word[::-1] for word in words]
        # 将单词重新组合成字符串
        return ' '.join(words)
```