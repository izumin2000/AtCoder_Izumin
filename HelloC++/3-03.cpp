#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    map<int, int> m;

    int n;
    cin >> n;

    int maxkey, maxvalue = 0;
    rep(_, n){
        int i;
        cin >> i;

        if (m.count(i)){
            m.at(i)++;
            if (m.at(i) > maxvalue){
                maxkey = i;
                maxvalue = m.at(i);
            }
        } else {
            m[i] = 1;
            if (maxvalue == 0){
                maxkey = i;
                maxvalue = 1;
            }
        }
    }

    cout << maxkey << " " << maxvalue << endl;
}