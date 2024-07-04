/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptrptr) {}
 *     ListNode(int x) : val(x), next(nullptrptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);

        ListNode *curr = head->next;
        int sum = 0;
        ListNode* newHead = nullptr;
        ListNode* newCurr = nullptr;
        while (curr != nullptr) {
            if (curr->val != 0) {
                sum += curr->val;
                curr = curr->next;
                continue;
            }
            ListNode* newNode = new ListNode(sum);
            sum = 0;
            if (newHead == nullptr) {
                newHead = newNode;
                newCurr = newNode;
            } else {
                newCurr->next = newNode;
                newCurr = newCurr->next;
            }
            curr = curr->next;
        }
        return newHead;
    }
};