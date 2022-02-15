#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n, a, b;
    cin >> n;

    vector <pair<int, int>> l(n);

    rep(i, n){
        cin >> a >> b;
        l.at(i) = make_pair(b, a);
    }

    sort(l.begin(), l.end());

    rep(i, n){
        cout << l.at(i).second << " " << l.at(i).first << endl;
    }
}