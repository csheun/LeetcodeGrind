class Solution {
public:

    bool checkHorizontal(vector<vector<char>>& board) {
        for (auto row : board) {
            bool nums_arr[10] = {false};
            for (char c : row) {
                if (c != '.') {
                    int num = c - '0';
                    if (nums_arr[num]) {
                        return false;
                    }
                    nums_arr[num] = true;
                } 
            }
        }
        return true;
    }

    bool checkVertical(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            bool nums_arr[10] = {false};
            for (int j = 0; j < 9; j++) {
                char c = board[j][i];
                if (c != '.') {
                    int num = c - '0';
                    if (nums_arr[num]) {
                        return false;
                    }
                    nums_arr[num] = true;
                }
            }
        }
        return true;
    }

    bool checkGrid(vector<vector<char>>& board) {
        const int gridSize = 3;

        for (int gridCol= 0; gridCol < gridSize; gridCol++) {
            for (int gridRow = 0; gridRow < gridSize; gridRow++) {
                bool nums_arr[10] = {false};
                for (int col = 0; col < gridSize; col++) {
                    for (int row = 0; row < gridSize; row++) {
                        int r = row + gridRow * gridSize;
                        int c = col + gridCol * gridSize;
                        char box = board[r][c];
                        if (box != '.') {
                            int num = box - '0';
                            if (nums_arr[num]) {
                                return false;
                            }
                            nums_arr[num] = true;
                        }
                    }
                }
            }
        }
        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        bool cond_1 = checkHorizontal(board);
        bool cond_2 = checkVertical(board);
        bool cond_3 = checkGrid(board);

        return cond_1 && cond_2 && cond_3;
    }
};