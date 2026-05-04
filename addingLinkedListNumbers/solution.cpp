#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;             
        ListNode* tail = &dummy;    
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int x = (l1 ? l1->val : 0);
            int y = (l2 ? l2->val : 0);
            int sum = x + y + carry;

            carry = sum / 10;
            int digit = sum % 10;

            tail->next = new ListNode(digit);
            tail = tail->next;

            if (l1){
                l1 = l1->next;
            }

            if (l2){
                l2 = l2->next;
            } 
            
        }
        return dummy.next;
    }

    void printList(ListNode* head) {
        while (head != nullptr) {
            cout << head->val << " ";
            head = head->next;
        }
        cout << endl;
    }
};

int main() {

    ListNode* l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);

    ListNode* l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);

    Solution s1;
    ListNode* result = s1.addTwoNumbers(l1, l2);

    s1.printList(result);

    return 0;
}
