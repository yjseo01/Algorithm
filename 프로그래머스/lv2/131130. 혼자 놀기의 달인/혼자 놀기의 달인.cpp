#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int visited[101] = {0, };

int dfs(vector<int> cards, int n, int cnt) {
    int ans = cnt;
    
    if (visited[cards[n] - 1] == 0) {
        visited[cards[n] - 1] = 1;
        ans = dfs(cards, cards[n] - 1, cnt + 1);
    } 
    
    return ans;
}

int solution(vector<int> cards) {
    int answer = 0;
    vector<int> lengths;
    
    for (int i = 0; i < cards.size(); i++) {
        if (visited[cards[i] - 1] == 0) {
            visited[cards[i] - 1] = 1;
            lengths.push_back(dfs(cards, cards[i] - 1, 1));
        }
    }
    
    sort(lengths.begin(), lengths.end());
    
    answer = lengths[lengths.size() - 1] * lengths[lengths.size() - 2];
    
    return answer;
}