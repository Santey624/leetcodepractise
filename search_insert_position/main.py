# 35. Search Insert Position
# Easy
# This problem belongs to the classic binary search problem

# Topics
# premium lock icon
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


class A:
    def search_inser_position(self, nums: list[int], target: int) -> int:
        low=0
        high = len(nums)-1
        
        while low <=high:
            middle = (low+high)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle -1
            else:
                low = middle +1
        # if the target is not found, return the index where it would be if it were inserted in order
        return low

a = A()
print(a.search_inser_position([1,3,5,6], 5))
print(a.search_inser_position([1,3,5,6], 2))
print(a.search_inser_position([1,3,5,6], 7))


# so this is the solution for the problem with O(log(m)) time complexity and this is the best solution for the problem