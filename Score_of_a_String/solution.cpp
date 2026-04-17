#include<iostream>
#include<string>
using namespace std;

int scoreOfString(string s) {
    int score = 0;
    for(int i = 0; i<s.size()-1; i++){
        int diff = abs(s[i]-s[i+1]);
        score = score + diff;
    }
    return score;
}

int main(){
    cout<<scoreOfString("hello");
    return 0;
}