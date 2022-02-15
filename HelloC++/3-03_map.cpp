// 最大最小を使わない場合はunordered_mapを使う

#include <bits/stdc++.h>
using namespace std;

int main() {
    map<string, string> dict;

    dict["apple"] = "ringo";
    dict["banana"] = "banana";
    dict["grape"] = "budou";

    cout << dict.at("grape") << endl;
    cout << dict["grape"] << endl;
    cout << dict.size() << endl;

    dict.erase("banana");       // 削除
    cout << dict.size() << endl;

    if (dict.count("apple")){
        cout << "there is a apple" << endl;
    } else {
        cout << "there isn\'t a apple" << endl;
    }
    
    if (dict.count("banana")){
        cout << "there is a banana" << endl;
    } else {
        cout << "there isn\'t a banana" << endl;
    }
    cout << endl;

    for (auto p : dict){
        cout << p.first << " " << p.second<< endl;
    }
}