#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n;
    int64_t a = 2, b = 1, tmp;
    cin >> n;

    rep(i, n){
        tmp = a + b;
        a = b;
        b = tmp;
        // cout << a << " " << b << endl;
    }
    cout << a << endl;
}