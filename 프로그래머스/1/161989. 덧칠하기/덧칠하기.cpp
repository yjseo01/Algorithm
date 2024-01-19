#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    int s = section.size();
    vector<int> visited(n + 1, 0);
    for (int i = 0; i < s; i++) {
        if (visited[section[i]] == 0) {
            for (int j = 0; j < m; j++) {
                if (section[i] + j > n) 
                    break;
                visited[section[i] + j] = 1;
            }
            answer += 1;
        }
    }
    return answer;
}