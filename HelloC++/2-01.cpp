#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n = 5;
    vector<int> l(n);
    
    rep(i, n){
        cin >> l.at(i);
    }

    int be = -1;
    int cond = false;
    for (int i : l){
        if (be == i){
            cond = true;
            break;
        }
        be = i;
    }

    if (cond){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}