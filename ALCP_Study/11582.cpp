// silver 4
// 치킨 TOP N
// https://www.acmicpc.net/problem/11582

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {

    int n;
    cin >> n;

    vector<int> chickenScore(n);
    for(int i=0; i<n; i++) {
        cin >> chickenScore[i];
    }

    int k;
    cin >> k;

    int groupSize = n / k;

    for(int i=0; i<n; i+=groupSize) {
        sort(chickenScore.begin() + i, chickenScore.begin() + i + groupSize);
    }

    for(int i=0; i<n; i++) {
        cout << chickenScore[i] << " ";
    }
    cout << endl;

    return 0;
}