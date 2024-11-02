class Solution {
public:
    bool isCircularSentence(string sentence) {
        bool cond_1 = sentence[0] == sentence[sentence.length() - 1];
        if (cond_1 == false) return false;
        bool cond_2 = false;

        char prev;
        bool check{false};
        for (auto c : sentence) {
            if (check) {
                if(c != prev) return false;
                prev = c;
            }
            if (c != ' ') {
                prev = c;
                check = false;
            } else {
                check = true;
            }
        }
        return true;

    }
};