X_train = [
    [1,3],
    [1,4],
    [2,3],
    [2,4],
    [3,1],
    [3,2],
    [4,1],
    [4,2]
]

y_train = [0, 1, 1, 1, 1, 1, 2, 2]

X_test = [
    [1,5],
    [5,1] 
]

y_test = [0, 1]


class KNN:
    def __init__(self, k: int) -> None:
        assert k > 0
        self.k = k
    
    def fit(self, X_train: list[tuple[int, int]], y_train: list[int]) -> None:
        self.X_train = X_train
        self.y_train = y_train
        
    def predict(self, X_test: list[tuple[int, int]]) -> list[int]:
        predict_label = []
        for cur_test in X_test:
            cur_dists = []
            for ind, cur_train in enumerate(self.X_train):
                cur_dist = ((cur_test[0] - cur_train[0]) ** 2 \
                    + (cur_test[1] - cur_train[1]) ** 2) ** 0.5
                  
                cur_dists.append((cur_dist, ind))
            
            cur_dists.sort(key=lambda x: x[0])
            
            clss_cnt = dict()
            for dist, ind in cur_dists[: self.k]:
                cur_clss = self.y_train[ind]
                if cur_clss not in clss_cnt:
                    clss_cnt[cur_clss] = 0
                clss_cnt[cur_clss] += 1
                
            best_clss = None
            best_cnt = 0
            for clss, cnt in clss_cnt.items():
                if best_clss is None:
                    best_clss = clss
                    best_cnt = cnt
                    continue
                
                if cnt > best_cnt:
                    best_clss = clss
                    best_cnt = cnt
            
            predict_label.append(best_clss)
        
        return predict_label
                
                
    
knn = KNN(2)
knn.fit(X_train, y_train)

predict_label = knn.predict(X_test)

print(predict_label)
            
            
        
            
    