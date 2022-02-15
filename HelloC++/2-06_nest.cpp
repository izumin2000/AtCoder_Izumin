// APG4b_v - 2-06

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)


int sigma(int a, int b){
    if (a == b) {
        return b;
    } else {
        return sigma(a + 1, b) + a;
    }
}

int my_sum(vector<int> xs){
    if (xs.size() == 1){
        return xs.at(0);
    } else {
        int ad = xs.at(xs.size() - 1);
        xs.pop_back();
        return my_sum(xs) + ad;
    }
}

/*
void printList(vector<int> &l){
    rep(i, l.size()){
        cout << l.at(i) << " ";
    }
    cout << endl;
}
*/

int main() {
    vector<int> l = {2, 3, 4, 1};
    cout << sigma(2, 9) << endl;
    cout << my_sum(l) << endl;
}