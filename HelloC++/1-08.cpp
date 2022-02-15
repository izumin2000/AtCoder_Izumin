#include <bits/stdc++.h>
using namespace std;

int main() {
    int p;
    cin >> p;

    if (p == 2) {
        string s;
        cin >> s;

        cout << s << "!" << endl;
    }

    int price, n;
    cin >> price >> n;

    cout << price * n << endl;
}