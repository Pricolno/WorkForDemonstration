class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        word_rightInp = dict()
        s_size = len(s)
        for ind in range(s_size - 1, -1, -1):
            ch = s[ind]
            if ch not in word_rightInp:
                word_rightInp[ch] = ind
        
        ans_bounds = []
        r_bound = 0
        l_bound = 0
        for ind in range(s_size):
            r_bound = max(r_bound, word_rightInp[s[ind]])
            if r_bound == ind:
                ans_bounds.append(r_bound - l_bound + 1)
                l_bound = ind + 1
        return ans_bounds