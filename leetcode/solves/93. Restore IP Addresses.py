class Solution:
    def rec_get_num(self, global_s: str, start: int,
            cur_nums_ip: list[int], need_deth, ans:list[str]):
        # print(start, need_deth, global_s)
        if need_deth == 0:
            if start == len(global_s):
                ans.append('.'.join(cur_nums_ip))
            
            return 

        if start == len(global_s):
            return
        

        
        end = start
        
        while end < len(global_s):
            end += 1
            if int(global_s[start:end]) <= 255:
                if end - start >= 2:
                    if global_s[start] == '0':
                        return
                cur_nums_ip.append(global_s[start:end])
                self.rec_get_num(global_s, end, cur_nums_ip, need_deth - 1, ans)
                cur_nums_ip.pop()
            else:
                return

    def restoreIpAddresses(self, s: str) -> List[str]:
        # 4 ровно числа нужна откусить, так чтобы все цифры использовались
        all_ip = []
        cur_nums_ip = []
        self.rec_get_num(
            global_s=s,
            start=0,
            cur_nums_ip=cur_nums_ip,
            need_deth=4,
            ans=all_ip
        )
        return all_ip