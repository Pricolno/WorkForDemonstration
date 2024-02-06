class Solution:
    @staticmethod
    def key_from_str(s: str) -> tuple:
        res_key = [0 for _ in range(ord('z') - ord('a') + 1)]
        for ch in s:
            res_key[ord(ch) - ord('a')] += 1
        return tuple(res_key)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_listStr = dict()
        for s in strs:
            key = Solution.key_from_str(s)
            if key not in key_listStr:
                key_listStr[key] = []
            key_listStr[key].append(s)
        
        return key_listStr.values()