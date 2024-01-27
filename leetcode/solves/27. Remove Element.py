class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n_size = len(nums)
        r_ind = n_size
        for l_ind in range(n_size):
            if nums[l_ind] != val:
                continue

            while r_ind == n_size or nums[r_ind] == val:
                if r_ind == -1:
                    break
                
                r_ind -= 1
            
            if l_ind  >= r_ind:
                break
            
            if nums[l_ind] == val:
                nums[l_ind], nums[r_ind] = \
                    nums[r_ind], nums[l_ind]

        return r_ind + 1