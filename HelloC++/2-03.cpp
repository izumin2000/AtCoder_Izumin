#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector <char>> l(n, vector<char>(n, '-'));
    
    int win, lose;
    rep(i, m){
        cin >> win >> lose;

        l.at(win - 1).at(lose - 1) = 'o';
        l.at(lose - 1).at(win - 1) = 'x';
    }

    rep(i, n){
        rep(j, n){
            if (j != (n - 1)) {
                cout << l.at(i).at(j) << ' ';
            } else {
                cout << l.at(i).at(j);
            }
        }
        cout << endl;
    }
}
