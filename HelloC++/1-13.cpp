#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n;
    int sum = 0, mean;
    cin >> n;

    vector<int> l(n);
    
    rep(i, n){
        cin >> l.at(i);
        sum += l.at(i);
    }

    mean = sum / n;

    rep(j, n){
        int abs = mean - l.at(j);

        if (abs < 0){
            abs *= -1;
        }

        cout << abs << endl;
    }
}