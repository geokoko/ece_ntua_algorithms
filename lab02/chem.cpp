#pragma GCC optimize("Ofast,unroll-loops,no-stack-protector")
#include <iostream>
#include <cstdio>
#include <climits>
#include <cstring>

#define ll long long
#define INF (LLONG_MAX / 4)

/* Using static long long arrays to avoid vector overhead
 */
static ll A[2505][2505];
static ll dp[2505][701];
static ll costArr[2505][2505];

void dc_dp(ll k, ll left, ll right, ll optLeft, ll optRight, ll N) {
    if (left > right) return;

    ll mid = (left + right) >> 1;
    ll bestPos = -1;
    ll bestVal = INF;

    for (ll i = optLeft; i <= std::min(mid - 1, optRight); i++) {
        ll val = dp[i][k - 1] + costArr[i + 1][mid];
        if (val < bestVal) {
            bestVal = val;
            bestPos = i;
        }
    }

    dp[mid][k] = bestVal;

    if (bestPos == -1) {
        bestPos = optLeft;
    }

    dc_dp(k, left, mid - 1, optLeft, bestPos, N);
    dc_dp(k, mid + 1, right, bestPos, optRight, N);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    ll N, K;
    scanf("%lld %lld", &N, &K);

    memset(A, 0, sizeof(A));
    for (ll i = 1; i < N; i++) {
        for (ll j = 1; j <= N - i; j++) {
            ll val;
            scanf("%lld", &val);
            A[i][i + j] = val;
            A[i + j][i] = val;
        }
    }
    // dp[i][k] => the minimal cost of placing i items into k flasks
    for (ll i = 0; i <= N; i++) {
        for (ll k_ = 0; k_ <= K; k_++) {
            dp[i][k_] = INF;
        }
    }
    dp[0][0] = 0; // 0 items in 0 flasks means 0 cost

    // precompute costs (cost of an interval [l, r] is the cost of interval [l, r - 1] + cost of adding r)
    // We'll do it on the fly to avoid huge colSum[][] array
    memset(costArr, 0, sizeof(costArr));  // set all costArr to 0

    for (ll r = 1; r <= N; r++) {
        static ll colSum[2505]; 
        memset(colSum, 0, sizeof(colSum));

        // fill colSum[] for A[l][r]
        for (ll l = r - 1; l >= 1; l--) {
            colSum[l] = colSum[l + 1] + A[l][r];
        }

        // now fill costArr[l][r] for l <= r
        costArr[r][r] = 0;  // interval of length 1
        for (ll l = r - 1; l >= 1; l--) {
            costArr[l][r] = costArr[l][r - 1] + colSum[l];
        }
    }

    // If we have 1 flask, we put all the chemicals in it
    for (ll i = 1; i <= N; i++) {
        dp[i][1] = costArr[1][i];
    }

    for (ll kVal = 2; kVal <= K; kVal++) {
        dc_dp(kVal, 1, N, 1, N, N);
    }

    printf("%lld\n", dp[N][K]);
    return 0;
}

