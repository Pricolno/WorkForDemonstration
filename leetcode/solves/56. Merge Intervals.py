class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for start, end in intervals:
            events.append((start, -1))
            events.append((end, 1))

        events.sort()

        last_start = None
        open_cnt = 0
        union_events = []
        for cord, tp in events:
            if tp == -1:
                if last_start is None:
                    last_start = cord
                open_cnt += 1
            else:
                open_cnt -= 1
                if open_cnt == 0:
                    union_events.append([last_start, cord])
                    last_start = None
        
        return union_events