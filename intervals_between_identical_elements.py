# https://leetcode.com/problems/intervals-between-identical-elements/
'''
You are given a 0-indexed array of n integers arr.
The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.
Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].
Note: |x| is the absolute value of x.

Ex 1:
Input: arr = [2,1,3,1,2,3,3]
Output: [4,2,7,2,4,4,5]
Explanation:
- Index 0: Another 2 is found at index 4. |0 - 4| = 4
- Index 1: Another 1 is found at index 3. |1 - 3| = 2
- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
- Index 3: Another 1 is found at index 1. |3 - 1| = 2
- Index 4: Another 2 is found at index 0. |4 - 0| = 4
- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5

Ex 2:
Input: arr = [10,5,10,10]
Output: [5,0,3,4]
Explanation:
- Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
- Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
- Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
- Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4
'''

from typing import List
from collections import defaultdict


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        '''
        Using hash table to store idx of each identical elements
        Ex [2, 1, 3, 1, 2, 3, 3]
        => map = {
            2: [0, 4]
            1: [1, 3]
            3: [2, 5, 6]
        }
        
        Process each items in map
        We need to calculate distance between each elements for each idx
        Ex: 
        Idx 2: 3 + 4 = 7
        Idx 5: 3 + 1 = 4
        Idx 6: 4 + 1 = 5
        We have ans for idx 2 = 7
        Ans for idx 5 = ans idx 2 + (number of idx before 2) * |5-2| - number of idx after (number of idx before 5) * |5-2|
        #     current_idx_ans += (idx - 1) * distance_before - (len(arr_value) - idx - 1) * distance_before
        # <=> current_idx_ans += (2 * idx - len(arr_value)) * distance_before
        
        Time complexity O(n)
        Space complexity O(n)
        '''
        ans = [0] * len(arr)
        dd = defaultdict(list)
        # O(n)
        for idx in range(len(arr)):
            dd[arr[idx]].append(idx)

        # O(n) each element will be traversaled just 2 time
        for arr_value in dd.values():
            current_idx_ans = 0
            for idx in range(1, len(arr_value)):
                current_idx_ans += arr_value[idx] - arr_value[0]
            ans[arr_value[0]] = current_idx_ans

            for idx in range(1, len(arr_value)):
                distance_before = arr_value[idx] - arr_value[idx - 1]
                # temp_sum += (idx - 1) * distance_before -(len(arr_value) - idx - 1) * distance_before
                current_idx_ans += (2 * idx - len(arr_value)) * distance_before
                ans[arr_value[idx]] = current_idx_ans

        return ans
