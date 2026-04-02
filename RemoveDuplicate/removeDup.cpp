#include <iostream>
#include <vector>
using namespace std;



// Brute force

int removeDup(vector<int> &nums) {
    int n = nums.size();
    int k = 0;
    for (int i = 0; i < n; i++) {
        bool duplicate = false;
        for (int j = 0; j < i; j++) {
            if (nums[i] == nums[j]) {
                duplicate = true;
                break;
            }
        }
        if (!duplicate) {
            nums[k] = nums[i];  
            k++;
        }
    }
    return k; 
}


// Efficient

// vector<int> removeDuplicate(vector<int> &nums) {
//     for (int i = 0; i < nums.size(); i++) {
//         for (int j = i + 1; j < nums.size(); j++) {
//             if (nums[i] == nums[j]) {
//                 nums.erase(nums.begin() + j);
//                 j--;
//         }
//     }
//     return nums;
//     }
// }
int main(){
    vector<int> a = {2, 3, 4, 2};
    int result = removeDup(a);

    for (int i = 0; i < result; i++) {
        cout << a[i] << " ";
    }
    return 0;
}
