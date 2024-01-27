# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1143619840
"""Beats
99.88%
of users with Python3"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_ind = 0
        r_ind = 0
        l_max_ind = 0
        r_max_ind = 0

        n_size = len(s)
        ch_set = set()
        while r_ind < n_size:
            while r_ind < n_size:
                if s[r_ind] not in ch_set:
                    ch_set.add(s[r_ind])
                    r_ind += 1
                else:
                    break
            
            if len(ch_set) > r_max_ind - l_max_ind:
                l_max_ind = l_ind
                r_max_ind = r_ind

            ch_set.discard(s[l_ind])
            l_ind += 1
        
        return r_max_ind - l_max_ind

                