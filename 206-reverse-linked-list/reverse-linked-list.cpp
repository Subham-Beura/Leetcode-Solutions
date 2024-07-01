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
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // if(!head)
        //     return NULL;
        // ListNode* prev=NULL;
        // ListNode* curr=head;
        // ListNode* next=curr->next;



        // while(curr){
        //     ListNode* next=curr->next;

        //     curr->next=prev;

        //     prev=curr;
        //     curr=next;
        // }
        // return prev; 
        if (!head)
            return nullptr;
        if (!head->next)
            return head;
        ListNode* reversedListLast=head->next;
        ListNode* reversed=reverseList(head->next);
        reversedListLast->next=head;
        head->next=nullptr;
        return reversed;
    }
};