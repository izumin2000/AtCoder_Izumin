#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    // vector<int> vec(3);      {0, 0, 0}
    // vector<int> vec = {1, 2, 3};

    vector<int> l(3, 2);      // {2, 2, 2}
    cout << l.at(0) << l.at(1) << l.at(2) << endl;

    l.at(0) = 3;        // {3, 2, 2}
    cout << l.at(0) << l.at(1) << l.at(2) << endl;

    l.push_back(1);;    // {3, 2, 2, 1}
    cout << l.at(0) << l.at(1) << l.at(2) << l.at(3) << endl;

    l.pop_back();;    // {3, 2, 2}
    l.pop_back();;    // {3, 2}
    cout << l.at(0) << l.at(1) << endl;
}