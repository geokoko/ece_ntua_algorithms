#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, k;
        cin >> n >> k;
        int a[n];
        unordered_map<int, int> modk_count;
        unordered_map<int, int> modk_index;

        for (int j = 0; j < n; ++j) {
            cin >> a[j];
            int mod = a[j] % k;
            modk_count[mod]++;
            if (modk_count[mod] == 1) {
                modk_index[mod] = j + 1;
            }
        }

        int count = 0;
        int index = -1;

        for (const auto &p : modk_count) {
            if (p.second == 1) {
                count++;
                index = modk_index[p.first];
                break;
            }
        }

        if (count == 0) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
            cout << index << endl;
        }
    }

    return 0;
}

