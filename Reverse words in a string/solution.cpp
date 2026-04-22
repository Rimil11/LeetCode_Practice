#include <iostream>
#include <string>
using namespace std;

string reverseWords(string s){
    int i = s.size() - 1;
    int j = s.size() - 1;
    string output;

    while (i >= 0) {
        // skip spaces
        while (i >= 0 && s[i] == ' ') i--;

        if (i < 0) break;

        j = i;
        // find start of word
        while (j >= 0 && s[j] != ' ') j--;

        // substr(start, length)
        string word = s.substr(j + 1, i - j);

        if (!output.empty()) output += " ";
        output += word;

        i = j - 1;
    }

    return output;
}

int main() {
    string s = "the sky is blue";
    cout << reverseWords(s) << endl;  // Output: "blue is sky the"
    return 0;
}
