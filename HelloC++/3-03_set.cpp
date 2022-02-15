// 最大最小を使わない場合はunordered_setを使う

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    set<int> s;

    s.insert(1);
    s.insert(2);
    s.insert(3);
    s.insert(1);

    for(auto i : s) {
        cout << i << endl;          // 小さい順から取り出す
    }

    cout << endl << s.size() << endl;
    cout << s.count(1) << endl;
    cout << *begin(s) << endl;      // 最大値
    cout << *rbegin(s) << endl;     // 最小値

    s.erase(1);                     // 削除
    cout << endl << s.size() << endl;
}