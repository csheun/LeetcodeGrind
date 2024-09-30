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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // fastptr and slow ptr
        ListNode* prev = nullptr;
        ListNode* slowptr = head;
        ListNode* fastptr = head;
        for (int i = 0; i < n; i++) {
            fastptr = fastptr->next;
        }
        while (fastptr != nullptr) {
            prev = slowptr;
            slowptr = slowptr->next;
            fastptr = fastptr->next;
        }
        if (prev == nullptr) {
            return slowptr->next;
        } else {
            prev->next = slowptr->next;
        }
        return head;
    }
};