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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* start=head,*curr=head->next;
        int sum=0;
        ListNode* newHead=NULL;
        ListNode* newCurr=NULL;
        while(curr!=NULL){
            if(curr->val==0){
                ListNode* newNode=new ListNode(sum);
                sum=0;
                if(newHead==NULL){
                    newHead=newNode;
                    newCurr=newNode;
                }else{
                    newCurr->next=newNode;
                    newCurr=newCurr->next;
                }
                curr=curr->next;
                continue;
            }
            sum+=curr->val;
            curr=curr->next;
        }
        return newHead; 
        
    }
};