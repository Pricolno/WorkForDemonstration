import heapq

class CntWord:
    def __init__(self, cnt, word):
        self.cnt = cnt
        self.word = word
    
    def __lt__(self, other):
        if not self.cnt == other.cnt:
            return self.cnt < other.cnt
        
        return not (self.word < other.word)
 

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_cnt = dict()
        for word in words:
            if word not in word_cnt:
                word_cnt[word] = 0
            word_cnt[word] += 1
        h = []

        for word, cnt in word_cnt.items():
            heapq.heappush(h, CntWord(cnt, word))
            if len(h) == k + 1:
                heapq.heappop(h)
        
        return reversed([heapq.heappop(h).word for _ in range(len(h))])