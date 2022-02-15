#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

struct Parson{
    string name;
    int age;
    string san(){
        return name + " san";
    }
};

int main() {
    Parson kanata = {"kanata", 21};
    Parson kanami;

    kanami.name = "kanami";
    kanami.age = 19;

    cout << kanata.age << endl;
    cout << kanami.age << endl;
    cout << kanami.san() << endl;

}

