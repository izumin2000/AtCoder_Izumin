#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    stack<int> s;

    s.push(1);
    s.push(3);
    s.push(5);
    s.push(7);

    cout << s.top() << endl;
    cout << s.empty() << endl;      // からかどうか

    s.pop();
    cout << s.top() << endl;

    s.pop();
    s.pop();
    s.pop();
    cout << s.empty() << endl;
}