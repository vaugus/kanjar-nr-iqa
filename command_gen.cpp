#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(int argc, char** argv) {
    const int start = stoi(argv[1]);
    const int end = stoi(argv[2]);
    const int step = stoi(argv[3]);

    string res = " ";

    for (int i = start; i <= end; i += step) {
        res += to_string(i) + " ";
    }

    cout << res << endl;

    return 0;
}