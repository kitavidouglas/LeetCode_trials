'''
You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
Multiply your score by x.
Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [8,3,9,3,8], k = 2
Output: 81
Explanation: To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.
Example 2:

Input: nums = [19,12,14,6,10,18], k = 3
Output: 4788
Explanation: To get a score of 4788, we can apply the following operations: 
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.

'''

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # 1. Precompute prime scores for numbers up to max(nums).
        max_val = max(nums)
        prime_score = [0] * (max_val + 1)
        # Sieve to compute number of distinct prime factors for each number.
        is_prime = [True] * (max_val + 1)
        for i in range(2, max_val + 1):
            if is_prime[i]:
                # i is prime, mark multiples and add factor
                for j in range(i, max_val + 1, i):
                    prime_score[j] += 1
                    is_prime[j] = False
                # restore i itself to True for correctness (not needed for factor count)
                is_prime[i] = True
        
        # Compute prime score for each element in nums.
        ps = [prime_score[x] for x in nums]
        
        # 2. Compute frequency for each index using monotonic stacks.
        left = [-1] * n  # nearest index on left with ps >= ps[i]
        stack = []
        for i in range(n):
            # For left boundary, we want the previous index with ps[j] >= ps[i]
            while stack and ps[stack[-1]] < ps[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        right = [n] * n  # nearest index on right with ps > ps[i]
        stack = []
        for i in range(n-1, -1, -1):
            # For right boundary, we want next index with ps[j] > ps[i]
            while stack and ps[stack[-1]] <= ps[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Frequency for each index i:
        freq = [ (i - left[i]) * (right[i] - i) for i in range(n) ]
        
        # 3. Build a list of (value, frequency) pairs.
        # We only care about numbers > 1 because multiplying by 1 doesn't change the score.
        cand = []
        for i in range(n):
            if nums[i] > 1:
                cand.append((nums[i], freq[i]))
        # Sort descending by value.
        cand.sort(key=lambda x: x[0], reverse=True)
        
        # 4. Greedily pick operations from the sorted candidates.
        ans = 1
        operations = k
        for val, f in cand:
            if operations <= 0:
                break
            # Use as many operations as possible for this candidate.
            count = min(f, operations)
            # Multiply answer by (val^count) mod MOD.
            ans = (ans * pow(val, count, MOD)) % MOD
            operations -= count
        
        return ans

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumScore([8, 3, 9, 3, 8], 2))  # Output: 81
    print(sol.maximumScore([19, 12, 14, 6, 10, 18], 3))  # Output: 4788
