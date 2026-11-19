class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_counts = {0: 1}
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
           
            diff = current_sum - k
            if diff in sum_counts:
                count += sum_counts[diff]
                
           
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1
            
        return count