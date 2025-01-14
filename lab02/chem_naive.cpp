#include <iostream>
#include <vector>

int main () {
	int N, K;
	std::cin >> N >> K;
	std::vector<std::vector<int>> A(N, std::vector<int>(N, 0));

	for (int i = 0; i < N - 1; i++) {
		for (int j = 0; j < N - i - 1; j++) {
			int val;
			std::cin >> val;
			A[i][j + i + 1] = val;
			A[j + i + 1][i] = val;
		}
	}

	int dp[N + 1][K + 1];
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= K; j++) {
			dp[i][j] = 1e9;
		}
	}
	std::vector<int> prefix_cost;
	std::vector<std::vector<int>> cost(N + 1, std::vector<int>(N + 1, 0));

	// precompute costs
	for (int l = 1; l <= N; l++) {
    	int sum_for_new_end = 0;
    	for (int r = l; r <= N; r++) {
        	sum_for_new_end = 0;
        	for (int i = l; i < r; i++) {
            	sum_for_new_end += A[i-1][r-1];
        	}
        	cost[l][r] = (r == l) ? 0 : cost[l][r-1] + sum_for_new_end;
    	}
	}

	dp[0][0] = 0;
	// If we have 1 flask, we put all the chemicals in it
	for (int i = 1; i <= N; i++) {
		dp[i][1] = cost[1][i];
	}

	for (int k = 2; k <= K; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j < i; j++) {
				dp[i][k] = std::min(dp[i][k], dp[j][k - 1] + cost[j + 1][i]);
			}
		}
	}

	std::cout << dp[N][K] << std::endl;
	return 0;
}
