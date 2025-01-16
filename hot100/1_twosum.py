from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in record:
                return [record[complement], i]
            else:
                record[nums[i]] = i
        return []

# Test the twoSum function
if __name__ == "__main__":
    # Define test cases
    test_cases = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1]
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2]
        },
        {
            "nums": [3, 3],
            "target": 6,
            "expected": [0, 1]
        }
    ]

    # Create an instance of Solution
    solution = Solution()

    # Iterate through each test case
    for idx, case in enumerate(test_cases):
        nums = case["nums"]
        target = case["target"]
        expected = case["expected"]
        result = solution.twoSum(nums, target)
        print(f"Test Case {idx + 1}:")
        print(f"Input nums = {nums}, target = {target}")
        print(f"Expected Output: {expected}")
        print(f"Actual Output:   {result}")
        print(f"Test {'Passed' if result == expected else 'Failed'}\n")
