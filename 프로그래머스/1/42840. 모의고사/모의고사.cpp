#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> p1 = {1, 2, 3, 4, 5};
    vector<int> p2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    vector<int> points = {0, 0, 0};
    
    for (int i = 0; i < size(answers); i++) {
        if (p1[i % 5] == answers[i]) {
            points[0]++;
        }
        if (p2[i % 8] == answers[i]) {
            points[1]++;
        }
        if (p3[i % 10] == answers[i]) {
            points[2]++;
        }
    }
    
    int maxans = 0;
    
    for (int i = 0; i < 3; i++) {
        if (maxans < points[i]) {
            maxans = points[i];
        }
    }
    
    int idx = 0;
    
    for (int i = 0; i < 3; i++) {
        if (maxans == points[i]) {
            answer.push_back(i + 1);
        }
    }
    
    
    return answer;
}