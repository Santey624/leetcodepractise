# Searching Algorithms


 #704. Binary Search
#Easy
#Topics
#premium lock icon
#Companies
#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

 

#Example 1:

#Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in nums and its index is 4
#Example 2:

#Input: nums = [-1,0,3,5,9,12], target = 2
#Output: -1
#Explanation: 2 does not exist in nums so return -1

class solution:
    # This solution is the solution for O(n) time complexity, which is not the best solution for the problem
    def binary_search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
    # This solution is the solution for O(log(n)) time complexity, which is the best solution for the problem
    def best_binary_search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            middle = (low+high)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle -1
            else:
                low = middle + 1
        return -1

if __name__ == "__main__":
    a = solution()
    print(a.best_binary_search([-1,0,3,5,9,12], 9))
    print(a.best_binary_search([-1,0,3,5,9,12], 2))

# But here is one thing to note
# This is not the best way to solve this searching algorithm
# In free time, we can try to solve this problem using binary search algorithm more efficiently

