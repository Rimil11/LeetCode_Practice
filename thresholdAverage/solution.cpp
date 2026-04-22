#include<iostream>
#include<vector>
#include<numeric>
using namespace std;

int numOfSubarrays(vector<int>& arr, int k, int threshold) {
    int currSum = accumulate(arr.begin(), arr.begin()+k, 0); 
    int count = 0;
    int value = k*threshold;
    if(currSum>=(value)){
        count += 1;
    }
    for(int i = 1; i<=arr.size()-k;i++){
        currSum -= arr[i-1];
        currSum += arr[i+k-1];
        if(currSum>=(value)){
            count += 1;
        }
    }
    return count;
}

int main(){
    vector<int> arr = {2,2,2,2,5,5,5,8};
    cout<<numOfSubarrays(arr, 3, 4);
    return 0;
}