class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m=board.size(),n=board[0].size();
        vector<vector<int>> a=board;
        int dx[]={-1,-1,-1,0,0,1,1,1};
        int dy[]={-1,0,1,-1,1,-1,0,1};

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int cnt=0;
                for(int k=0;k<8;k++){
                    int x=i+dx[k],y=j+dy[k];
                    if(x>=0&&x<m&&y>=0&&y<n&&a[x][y]==1)
                        cnt++;
                }
                if(a[i][j]==1){
                    if(cnt<2||cnt>3)
                        board[i][j]=0;
                }
                else{
                    if(cnt==3)
                        board[i][j]=1;
                }
            }
        }
    }
};