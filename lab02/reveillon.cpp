#include <cstdio>
#include <algorithm>
#include <climits>

using namespace std;

int main () {
	int N, K;
	scanf("%d %d", &N, &K);
	int h[N + 1];
	h[0] = -1;
	for (int i = 1; i <= N; i++) {
		scanf("%d", &h[i]);
	}

	int dp[N + 1]; // dp[i] is the maximum score that can be achieved with i people
	dp[0] = 0;     // Base case: 0 people, 0 score
	for (int i = 1; i < N + 1; ++i) {
		int max_here = 0;
		dp[i] = 0;  // Initialize for a new person i
		for (int j = 1; j <= min(K, i); ++j) {
			max_here = max(max_here, h[i - j + 1]); // Calculate the maximum in current table t 
			dp[i] = max(dp[i], dp[i - j] + j * max_here); // Update the current table
														  // so that the overall score is maximized
		}
	}

	printf("%d\n", dp[N]);

	return 0;
}
