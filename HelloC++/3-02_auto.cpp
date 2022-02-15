#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<pair<int, int>> l = {make_pair(1, 2), make_pair(3, 4), make_pair(5, 6)};
    
    for (auto p : l){       // pair<int, int>を自動判別
        cout << p.first << " " << p.second << endl;
    }
}