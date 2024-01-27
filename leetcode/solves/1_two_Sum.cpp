#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, vector<int>> num_cnt;
        for (int ind = 0; ind < static_cast<int>(nums.size()); ++ind) {
            if (num_cnt.find(nums[ind]) == num_cnt.end()) {
                num_cnt[nums[ind]] = vector<int>();
            }
            num_cnt[nums[ind]].push_back(ind);
        }

        for (int ind = 0; ind < static_cast<int>(nums.size()); ++ind) {
            int num_a = nums[ind];
            int num_b = target - num_a;
            if (num_a == num_b) {
                if (num_cnt[num_a].size() >= 2) {
                    return vector{num_cnt[num_a][0], num_cnt[num_a][1]};
                }
            } else {
                if (num_cnt.find(num_b) != num_cnt.end()) {
                    return vector{ind, num_cnt[num_b][0]};
                }
            }
        }

        return vector<int>{0, 1};
    }
};