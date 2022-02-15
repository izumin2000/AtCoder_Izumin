#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    pair<string, int> p("one", 1);
    cout << p.first << " " << p.second << endl;

    p = make_pair("two", 2);
    cout << p.first << " " << p.second << endl;

    string fir;
    int sec;
    tie(fir, sec) = p;
    cout << fir << " " << sec << endl;    
}