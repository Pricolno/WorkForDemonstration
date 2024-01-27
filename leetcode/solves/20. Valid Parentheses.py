class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def is_open(ch: str) -> bool:
            return ch == '[' \
            or ch == '(' \
            or ch == '{'

        def is_paired_close(l_ch, r_ch: str) -> bool:
            return (l_ch == '[' and r_ch == ']') \
            or (l_ch == '(' and r_ch == ')') \
            or (l_ch == '{' and r_ch == '}')

        
        for ch in s:
            if is_open(ch):
                stack.append(ch)
            else:
                if not stack \
                or not is_paired_close(stack[-1], ch):
                    return False
                else:
                    stack.pop()
        return not stack
