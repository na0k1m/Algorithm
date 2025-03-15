// bronze 2
// 하얀 칸
// https://www.acmicpc.net/problem/1100

#include <iostream>
using namespace std;

int main(void) {

    char chess[8][8];
    int cnt = 0;

    for(int i=0; i<8; i++) {
        for(int j=0; j<8; j++) {
            cin >> chess[i][j];
        }
    }

    for(int i=0; i<8; i++) {
        for(int j=0; j<8; j++) {
            if((i + j) % 2 == 0) {
                if(chess[i][j] == 'F') {
                    cnt++;
                }
            }
        }
    }

    cout << cnt << endl;

    return 0;
}