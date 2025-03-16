// silver 4
// 요세푸스 문제
// https://www.acmicpc.net/problem/1158

#include <iostream>
#include <vector>
using namespace std;

int main(void) {

    int n, k;
    cin >> n >> k;

    vector<int> circle;
    for(int i=0; i<n; i++) {
        circle.push_back(i+1);
    }

    vector<int>::iterator it = circle.begin();

    cout << "<";
    while(!circle.empty()) {
        for(int i=1; i<k; i++) {
            it++;
            if(it == circle.end()) {
                it = circle.begin();
            }
        }
        cout << *it;
        it = circle.erase(it);

        if(circle.empty()) {
            cout << ">" << endl;
        }
        else {
            cout << ", ";
            if(it == circle.end()) {
                it = circle.begin();
            }
        }
    }

    return 0;
}