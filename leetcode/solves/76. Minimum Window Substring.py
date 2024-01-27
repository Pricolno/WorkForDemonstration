class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wind_d_cnt = dict()
        temp_d_cnt = dict()
        for ch in t:
            if ch not in temp_d_cnt:
                temp_d_cnt[ch] = 0
            temp_d_cnt[ch] += 1
        t_size = len(t)
        s_size = len(s)

        l_ind, r_ind = 0, 0
        ans_l, ans_r = None, None
        cur_full_t = 0
        while l_ind < s_size:
            while cur_full_t < t_size and r_ind < s_size:
                r_ch = s[r_ind]
                r_ind += 1
                
                if r_ch not in wind_d_cnt:
                    wind_d_cnt[r_ch] = 0
                wind_d_cnt[r_ch] += 1
                if r_ch in temp_d_cnt \
                    and wind_d_cnt[r_ch] <= temp_d_cnt[r_ch]:
                   cur_full_t += 1
                
                if cur_full_t == t_size:
                    # if ans_l is None:
                    #     ans_l, ans_r = l_ind, r_ind
                    # else:
                    #     if ans_r - ans_l > r_ind - l_ind:
                    #         ans_l, ans_r = l_ind, r_ind
                    break

            if cur_full_t == t_size:
                if ans_l is None:
                    ans_l, ans_r = l_ind, r_ind
                else:
                    if ans_r - ans_l > r_ind - l_ind:
                        ans_l, ans_r = l_ind, r_ind
            
            l_ch = s[l_ind]
            l_ind += 1
            wind_d_cnt[l_ch] -= 1
            if l_ch in temp_d_cnt and wind_d_cnt[l_ch] < temp_d_cnt[l_ch]:
                cur_full_t -= 1
            
            # maybe del wind_d_cnt[l_ch] = 0

        if ans_l is None:
            return ""
        else:
            return s[ans_l: ans_r]
        