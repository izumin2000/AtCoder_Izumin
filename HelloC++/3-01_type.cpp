#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int64_t l = 123456789123456789LL;
    double d = 3.1415926535;

    cout << l << endl;
    cout << fixed << setprecision(10);
    cout << d << endl;

    string s = "123";
    int n = 123;
    cout << "0" + to_string(n) << endl;
    cout << stoi(s) + 1 << endl;
}