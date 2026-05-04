/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* deleteDuplicates(ListNode* head) {
    ListNode* curr = head;
    while (curr != nullptr && curr->next != nullptr) {
        if (curr->val == curr->next->val) {
            ListNode* temp = curr->next;
            curr->next = curr->next->next; 
            delete temp;                    
        } else {
            curr = curr->next;             
        }
    }
    return head;
}


void display(ListNode* head){
    ListNode* curr = head;
    while(curr!=nullptr){
        cout<<curr->val<<endl;
        curr = curr->next;
    }
}

int main(){
    ListNode* head = new ListNode(34);
    ListNode* ptr2 = new ListNode(36);
    ListNode* ptr3 = new ListNode(36);
    ListNode* ptr4 = new ListNode(36);
    
    head->next = ptr2;   // link them
    ptr2->next = ptr3;
    ptr3->next = ptr4;
    head = deleteDuplicates(head);
    display(head);

    return 0;
}
