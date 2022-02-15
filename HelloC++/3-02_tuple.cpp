#include <bits/stdc++.h>
using namespace std;

int main() {
    tuple<int ,bool, string> t(0, false, "zero");
    cout << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;

    t = make_tuple(1, true, "one");
    cout << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;

    int fir;
    bool sec;
    string tha;
    tie(fir, sec, tha) = t;
    cout << fir << " " << sec << " " << tha << endl;
}