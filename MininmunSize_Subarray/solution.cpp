#include <iostream>
#include <vector>
#include <climits>   // for INT_MAX
using namespace std;

int minSubArrayLen(int target, vector<int>& nums) {
    int n = nums.size();
    int left = 0, sum = 0;
    int minLen = INT_MAX;   // start with "infinity"

    for (int right = 0; right < n; right++) {
        sum += nums[right];   // expand window
        while (sum >= target) {
            minLen = min(minLen, right - left + 1); // update minimum length
            sum -= nums[left++]; // shrink window
        }
    }
    return (minLen == INT_MAX) ? 0 : minLen;
}

int main() {
    vector<int> nums = {2,3,1,2,4,3};
    int target = 7;
    cout << minSubArrayLen(target, nums) << endl; // Output: 2
}
