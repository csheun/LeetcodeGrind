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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || k == 0) {
            return head;
        }
        vector<ListNode*> vec;
        while (head != nullptr) {
            vec.push_back(head);
            head = head->next;
        }
        int count = vec.size();
        if (k % count == 0) {
            return vec[0];
        }
        int new_head_idx = count - (k % count);
        vec[count - 1]->next = vec[0];
        vec[new_head_idx - 1]->next = nullptr;
        return vec[new_head_idx];
    }
};