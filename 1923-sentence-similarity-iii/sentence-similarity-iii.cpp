class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        if (sentence1.length() == sentence2.length()) {
            return sentence1 == sentence2;
        }
        if (sentence1.length () > sentence2.length()) {
            string temp = sentence2;
            sentence2 = sentence1;
            sentence1 = temp;
        }
        vector<string> sen1_arr = tokenise(sentence1);
        vector<string> sen2_arr = tokenise(sentence2);

        if (sen1_arr[0] == sen2_arr[0]) {
            int sen1_idx = 0;
            for (const string& str : sen2_arr) {
                if (str == sen1_arr[sen1_idx]) {
                    sen1_idx++;
                    if (sen1_idx == sen1_arr.size()) {
                        return true;
                    }
                } else {
                    break;
                }
            }
            int j = sen1_arr.size() - 1;
            for (int i = sen2_arr.size() - 1; i >= 0; i--) {
                if (sen2_arr[i] == sen1_arr[j]) {
                    if (j == sen1_idx) {
                        return true;
                    } 
                    j--;
                } else {
                    return false;
                }
            }
            return false;

        } else {
            int sen1_idx = sen1_arr.size() - 1;
            for (int i = sen2_arr.size() - 1; i >= 0; i--) {
                if (sen2_arr[i] == sen1_arr[sen1_idx]) {
                    if (sen1_idx == 0) {
                        return true;
                    }
                    sen1_idx--;
                } else {
                    return false;
                }
            }
            return false;
        }
    }
    vector<string> tokenise(string sentence) {
        vector<string> res;
        string str;
        for (const char& c : sentence) {
            if (c == ' ') {
                res.push_back(str);
                str = "";
            } else {
                str += c;
            }
        } 
        res.push_back(str);
        return res;
    }
};