第一种写法，定义 target 是在一个在左闭右闭的区间里，也就是[left, right] 

区间的定义这就决定了二分法的代码应该如何写，因为定义target在[left, right]区间，所以有如下两点：

while (left <= right) 要使用 <= ，因为left == right是有意义的，所以使用 <=
可以是[1，1]来举例说明，因为左边和右边都包含1，所以可能left = right，即1=1
if (nums[middle] > target) right 要赋值为 middle - 1，因为当前这个nums[middle]一定不是target，
！！！要一直坚持左闭右闭的原则，以为已经确定nums[middle]是大于target，那么就应该选择下一位（middle-1）
那么接下来要查找的左区间结束下标位置就是 middle - 1
例如在数组：1,2,3,4,7,9,10中查找元素2，如图所示：
![Alt text](image.png)

class solution{
public:
    int search(vector<int>& nums, int target){
        int left = 0;
        int right = num.size() - 1;
        while(left<=right){
            int middle = left + ((right - left) / 2);
            if(nums[middle] > target){
                right = middle - 1;
            }
            else if(num[middle] < target){
                left = middle + 1;
            }
            else{
<!-- (num[middle] = target); -->
            return middle;
            }
        return 0;
    }
};


#二分法第二种写法
如果说定义 target 是在一个在左闭右开的区间里，也就是[left, right) ，那么二分法的边界处理方式则截然不同。
有如下两点：

while (left < right)，这里使用 < ,因为left == right在区间[left, right)是没有意义的
依然可以是[1，1)来举例说明，因为左边已经包含1，但是右边不包含1，所以不可能left = right
if (nums[middle] > target) right 更新为 middle，因为当前nums[middle]不等于target，去左区间继续寻找，而寻找区间是左闭右开区间，所以right更新为middle，即：下一个查询区间不会去比较nums[middle]
在数组：1,2,3,4,7,9,10中查找元素2，如图所示：（注意和方法一的区别）
![Alt text](image-1.png)
class solution{
public:
    int search(vector<int>& nums, int target){
        int left;
        int right = nums.size() - 1;
        while(left < right){
            int middle = left + ((right - left)+1);
            if(nums[middle] > target){
                right = middle
            }
            else if(nums[middle] < target){
                left = middle - 1;
            }
            else{
                return middle;
            }
        return 0;
        }
    }
}

