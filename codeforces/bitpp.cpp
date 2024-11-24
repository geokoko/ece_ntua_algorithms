#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main () {
	int N;
	int X = 0;
	cin >> N;

	string line;
	
	for (int i = 0; i < N; ++i) {
		cin >> line;
		line.erase(remove(line.begin(), line.end(), 'X'	), line.end());
		if (line == "++")
			++X;
		if (line == "--")
			--X;
	}

	cout << X << endl;
}
