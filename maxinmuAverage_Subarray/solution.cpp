#include<iostream>
#include<vector>
#include<numeric>
using namespace std;


double findMaxAverage(vector<int>& nums, int k){
    int currSum = accumulate(nums.begin(), nums.begin()+k, 0); 
    int larSum = currSum;
    
    for(int i = 1; i<=nums.size();i++){
        cout<<larSum<<endl;
        currSum += nums[i+k-1];
        currSum -= nums[i-1];
        larSum = max(currSum, larSum);
    }
    return static_cast<double>(larSum) / k;
}

int main(){
    vector<int> nums = {1,12,-5,-6,50,3};
    cout<<findMaxAverage(nums, 4);
    return 0;
}