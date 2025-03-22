// bronze 1
// N번째 큰 수
// https://www.acmicpc.net/problem/2693

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {

    int t;

    cin >> t;

    for(int i=0; i<t; i++) {
        vector<int> numList(10);
        for(int j=0; j<10; j++) {
            cin >> numList[j];
        }
        sort(numList.begin(), numList.end());
        cout << numList[7] << endl;
    }

    return 0;
}