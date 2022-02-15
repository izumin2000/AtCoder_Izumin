#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string s;
    cin >> s;

    string c;
    int n = 1;
    rep(i, s.size()){
        c = s.at(i);
        if (c == "+") {
            n++;
        } else if (c == "-") {
            n--;
        }
    }

    cout << n << endl;
}
