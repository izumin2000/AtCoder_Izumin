// デキューdeque：スタックとキューを合わせたデータ構造

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    deque<int> d;

    d.push_front(1);
    d.push_back(3);
    d.push_front(5);
    d.push_back(7);

    for(int i : d) {
        cout << i << endl;
    }
    cout << d.at(0) << endl << endl;        // 0番目を参照

    d.pop_front();
    d.pop_back();

    for(int i : d) {
        cout << i << endl;
    }
}