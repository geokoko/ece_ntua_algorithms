#include <iostream>
#include <cmath>
using namespace std;

int main () {
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i) {
		int n;
		cin >> n;

		int operations = 0;
		int covered = 1;
		while (covered < n) {
			operations++;
			covered *= 2;
		}

		cout << operations + 1 << endl;
	}

	return 0;
}
