class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n_size = len(nums)
        l_ind = 0
        r_ind = n_size
        while (r_ind - l_ind >= 2):
            m_ind = (r_ind + l_ind) // 2
            if target <= nums[-1]:
                if nums[m_ind] > nums[-1]:
                    l_ind = m_ind
                    continue
                if nums[m_ind] > target:
                    r_ind = m_ind
                else:
                    l_ind = m_ind
            else:
                if nums[m_ind] <= nums[-1]:
                    r_ind = m_ind
                    continue
                if nums[m_ind] > target:
                    r_ind = m_ind
                else:
                    l_ind = m_ind

        if nums[l_ind] == target:
            return l_ind
        else:
            return -1
     