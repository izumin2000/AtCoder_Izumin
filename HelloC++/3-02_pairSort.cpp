#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    pair<int, int> a(1, 2);
    pair<int, int> b(1, 3);
    pair<int, int> c(2, 1);

    if (a > b){
        cout << "a > b" << endl;
    } else {
        cout << "a < b" << endl;
    }

    if (a > c){
        cout << "a > c" << endl;
    } else {
        cout << "a < c" << endl;
    }

}