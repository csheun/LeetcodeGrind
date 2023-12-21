class Solution {
public:
    bool isValid(string s) {
        stack<char> brackets;

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                brackets.push(c);
            } else {
                if (brackets.empty()) {
                    return false;
                }
                char target = brackets.top();
                switch (c) {
                    case ')':
                        if (target != '(') {
                            return false;
                        }
                        break;
                    case ']':
                        if (target != '[') {
                            return false;
                        }
                        break;
                    case '}':
                        if (target != '{') {
                            return false;
                        }
                        break;
                }
                brackets.pop();
            }
        }

        if (brackets.empty()) {
            return true;
        }
        return false;
    }
};