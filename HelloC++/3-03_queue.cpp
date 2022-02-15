#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    // キュー
    queue<int> q;

    q.push(1);
    q.push(3);
    q.push(5);
    q.push(7);

    cout << q.front() << endl;
    q.pop();
    cout << q.front() << endl << endl;

    // 優先度付きキュー
    priority_queue<int> pq;

    pq.push(1);
    pq.push(3);
    pq.push(5);
    pq.push(7);

    cout << pq.top() << endl;   // 最大値を取得
    pq.pop();
    cout << pq.top() << endl << endl;


    // 優先度付きキュー（逆順）
    priority_queue<int, vector<int>, greater<int>> rpq;

    rpq.push(2);
    rpq.push(3);
    rpq.push(5);
    rpq.push(7);

    cout << rpq.top() << endl;   // 最大値を取得
    rpq.pop();
    cout << rpq.top() << endl;
}