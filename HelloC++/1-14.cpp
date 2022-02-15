#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n, m, l, mx, mn;
    cin >> n >> m >> l;

    mx = max(max(n , m), l);
    mn = min(min(n , m), l);

    cout << mx - mn << endl;
}