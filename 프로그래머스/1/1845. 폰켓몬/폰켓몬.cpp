#include <vector>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    vector<int> vec(200001, 0);
    
    for (int i: nums) {
        vec[i]++;
    }
    
    int k = nums.size() / 2;
    
    for (int j = 0; j < vec.size() && k > 0; j++) {
        if (vec[j] > 0) {
            vec[j]--;
            k--;
            answer++;
        }
    }
    
    return answer;
}