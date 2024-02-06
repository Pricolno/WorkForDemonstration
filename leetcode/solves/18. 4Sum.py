class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = dict()
        n_size = len(nums)

        num2ind = dict()
        for i, num in enumerate(nums):
            if num not in num2ind:
                num2ind[num] = set()
            if len(num2ind[num]) < 4:
                num2ind[num].add(i)


        for i_a in range(n_size):
            a = nums[i_a]
            for i_b in range(i_a + 1, n_size):
                b = nums[i_b]
                for i_c in range(i_b + 1, n_size):
                    c = nums[i_c]
                    
                    if target - (a + b + c) not in num2ind:
                        continue
                    
                    ids_d = num2ind[target - (a + b + c)]

                    for i_d in ids_d:
                        if len({i_a, i_b, i_c, i_d}) != 4:
                            continue
                        
                        d = nums[i_d]
                        if a + b + c + d != target:
                            continue
                    
                        ans[tuple(sorted((a, b, c, d)))] = True
        return ans.keys()