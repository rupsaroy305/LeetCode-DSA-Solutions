class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        vector<set<char>> r(9),c(9),b(9);
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]=='.')
                    continue;
                char x=board[i][j];
                int k=(i/3)*3+j/3;
                if(r[i].count(x)||c[j].count(x)||b[k].count(x))
                    return false;
                r[i].insert(x);
                c[j].insert(x);
                b[k].insert(x);
            }
        }
        return true;
    }
};