#include <bits/stdc++.h>
using namespace std;

struct Clock{
    int hour;
    int minute;
    int second;

    void set(int h, int m, int s){
        hour = h;
        minute = m;
        second = s;
    }

    string to_str(){
        string str;

        if (hour <= 9) {
            str = '0' + to_string(hour);
     
        } else {
            str = to_string(hour);
        }

        if (minute <= 9) {
            str += ":0" + to_string(minute);
        } else {
            str += ":" + to_string(minute);
        }

        if (second <= 9) {
            str += ":0" + to_string(second);
        } else {
            str += ":" + to_string(second);
        }

        return str;
    }

    void shift(int diff_second){
        int now = hour * 3600 + minute * 60 + second + diff_second;
        if (now < 0) {
            now += 86400;
        }

        hour = (int) now / 3600;
        minute = (int) (now%3600) / 60;
        second = now%60;

        if (hour == 24) {
            hour = 0;
        }
    }
};

int main() {
  // 入力を受け取る
  int hour, minute, second;
  cin >> hour >> minute >> second;
  int diff_second;
  cin >> diff_second;

  // Clock構造体のオブジェクトを宣言
  Clock clock;

  // set関数を呼び出して時刻を設定する
  clock.set(hour, minute, second);

  // 時刻を出力
  cout << clock.to_str() << endl;

  // 時計を進める(戻す)
  clock.shift(diff_second);

  // 変更後の時刻を出力
  cout << clock.to_str() << endl;
}
