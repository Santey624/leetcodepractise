class A:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(f"Answer is {nums[i], nums[j]}")
                    return [i, j]
                
i1 = A().twosum([2,7,11,15], 9)
print(i1)