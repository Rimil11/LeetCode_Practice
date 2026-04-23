#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isVowel(char c, const vector<char>& vowels) {
        return (c=='a'||c=='e'||c=='i'||c=='o'||c=='u');
    }

    int maxVowels(string s, int k){
        int i = 0;
        int j = k-1;
        int count = 0;
        int maxNum = 0;
        for(int l = i;l<=j;l++){
            if(isVowel(s[l])){
                count++;
            }
        }
        
        maxNum = count;
        while(j<s.size()-1){
            i++;
            j++;
            if(isVowel(s[i-1])){
                count--;
            }
            if(isVowel(s[j])){
                count++;
            }
            maxNum = max(count, maxNum);
        }
        return maxNum;
    }
};

int main() {
    Solution sol;
    string s = "k";
    int k = 3;
    cout << "Result: " << sol.maxVowels(s, k) << endl;
    return 0;
}
