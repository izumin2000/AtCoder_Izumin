#include <bits/stdc++.h>
using namespace std;

int refF(int &a){
    a *= 2;
    return a;
}

void vrefF(int &a){
    a *= 2;
}

int main() {
    int n = 3;
    int &m = n;

    n = 4;
    cout << n << endl;
    cout << m << endl << endl;

    m = 5;
    cout << n << endl;
    cout << m << endl << endl;

    int x = 3;
    int y = refF(x);
    cout << x << endl;
    cout << y << endl << endl;

    int z = 3;
    vrefF(z);
    cout << z << endl << endl;
}