#include <string>
#include <vector>
#define INF 1000000000

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = INF;
    int matrix[200][200];
    for (int i = 0; i < 200; ++i) {
        for (int j = 0; j < 200; ++j) {
            matrix[i][j] = INF;
        }
    }
    for (int i = 0; i < n; i++) {
        matrix[i][i] = 0;
    }
    
    for (int i = 0; i < fares.size(); i++) {
        int x = fares[i][0] - 1;
        int y = fares[i][1] - 1;
        matrix[x][y] = fares[i][2];
        matrix[y][x] = fares[i][2];
    }
    
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            if (matrix[i][k] != INF) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j]);
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        answer = min<long long>(answer, (long long)matrix[s - 1][i] + matrix[i][a - 1] + matrix[i][b - 1]);
    }
    return answer;
}