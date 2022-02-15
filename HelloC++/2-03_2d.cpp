#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    vector<vector<int>> l(2, vector<int>(3, 4));

    cout << l.size() << endl;
    cout << l.at(0).size() << endl;
    cout << l.size() * l.at(0).size() << endl;
    cout << l.at(0).at(0) << endl << endl;


    int n = 3;
    vector<vector<int>> JagLst(n);      // ジャグ配列
    rep(i, n){
        rep(j, (i + 1)){
            JagLst.at(i).push_back(j + 1);
        }
    }
    // JagLst = {{1}, {1, 2}, {1, 2, 3}}

    for (vector<int> Lst : JagLst){
        for (int k : Lst){
            cout << k << endl;
        }
    }
}