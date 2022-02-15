#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n, s;
    cin >> n >> s;

    vector<int> la(n);
    vector<int> lp(n);
    
    rep(i, n){
        cin >> la.at(i);
    }

    rep(j, n){
        cin >> lp.at(j);
    }

    int ans = 0;
    for (int i : la){
        for (int j : lp){
            if ((i + j) == s) {
                ans++;
            }
        }
    }

    cout << ans << endl;
}