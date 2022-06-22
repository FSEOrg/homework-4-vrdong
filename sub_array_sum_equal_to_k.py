from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Sum from idx_a to idx_b = prefix_sum_b - prefix_sum_a  | idx_a < idx_b
        Example 
        [1,2,3] => prefix_sum_array [1,3,6]
        sum from idx 0->1 = prefix_sum[1] - prefix_sum[0] = 3-1 = 2
        
        I create array prefix_sum first 
        I traversal from left to right of array prefix_sum. 
        Assume i have value in prefix_sum is a
        I need to find how many prefix sum have value is a - k before index of a.
        I use hashmap to support this job
        
        Time complexity O(2n) => 0(n) 
        Space complexity O(n) 
        '''
        prefix_sum_arr = []
        prefix_sum = 0
        ans = 0
        for val in nums:
            prefix_sum += val
            prefix_sum_arr.append(prefix_sum)
                    
        counter = defaultdict(int)
        counter[0] = 1
        
        for val in prefix_sum_arr:
            ans += counter[val - k]
            counter[val] += 1
        return ans
    