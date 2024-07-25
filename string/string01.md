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