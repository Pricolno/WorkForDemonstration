class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_size = len(s)
        # dp[len][l_ind]
        dp = [
            [False for _ in range(s_size)]
            for _ in range(s_size + 1)
        ]
        l_max_ind = 0
        r_max_ind = -1

        for len_ in range(1, s_size + 1):
            for l_ind in range(0, s_size):
                r_ind = l_ind + len_ - 1
                if r_ind >= s_size:
                    break
                
                if len_ == 1:
                    dp[len_][l_ind] = True
                elif len_ == 2:
                    dp[len_][l_ind] = s[l_ind] == s[r_ind]
                else:
                    if s[l_ind] == s[r_ind] \
                        and dp[len_ - 2][l_ind + 1]:
                        dp[len_][l_ind] = True
                
                if dp[len_][l_ind]:
                    if  r_max_ind - l_max_ind + 1 < len_:
                        l_max_ind = l_ind
                        r_max_ind = r_ind
        return s[l_max_ind: r_max_ind + 1]
                
                
