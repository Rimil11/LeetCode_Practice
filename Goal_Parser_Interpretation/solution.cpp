#include<iostream>
#include<string>
using namespace std;


string interpret(string command) {
    string output = "";
    for(int i = 0; i<command.size(); i++){
        if(command[i] == 'G'){
            output.push_back('G');
        }
        else if(command[i] == '('){
            if(command[i+1]==')'){
                output.push_back('o');
            }
            else{
                output += "al";
            }
        }
    }
    return output;
}

int main(){
    cout<<interpret("G()()()(al)");
    return 0;
}