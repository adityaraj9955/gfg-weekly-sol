from typing import List

class Solution:
    def maxSum(self, n: int, x: int, arr: List[int]) -> int:
        max_set = -1
        max_unset = -1
        x_bit = 1 << (x - 1)

        for num in arr:
            if num & x_bit:
                if num > max_set:
                    max_set = num
            else:
                if num > max_unset:
                    max_unset = num

        if max_set == -1 or max_unset == -1:
            return -1
        else:
            return max_set + max_unset
