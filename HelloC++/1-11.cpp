#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n, a;
    cin >> n >> a;

    rep(i, n){
        string op;
        int b;
        cin >> op >> b;

        if (op == "+"){
            a += b;
            cout << i + 1 << ":" << a << endl;
        } else if (op == "-"){
            a -= b;
            cout << i + 1 << ":" << a << endl;
        } else if (op == "*"){
            a *= b;
            cout << i + 1 << ":" << a << endl;
        } else if (op == "/"){
            if (b != 0){
                a /= b;
                cout << i + 1 << ":" << a << endl;
            } else {
                cout << "error" << endl;
                break;
            }
        }
    }
}