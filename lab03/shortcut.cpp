#include <cstdio>
#include <vector>
#include <utility>
#include <limits>
#include <queue>
#include <iostream>

#define ll long long

const ll INF = 1000000000000000000LL;

struct State {
	ll int_node;	/* current node */
	ll k;			/* how many edges have we skipped with superspeed */
	ll path_length;	/* path length */

	bool operator > (const State& other) const {
		return path_length > other.path_length;
	}	
};

int main () {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);

	ll N, M, s, t, B;
	scanf("%lld %lld %lld %lld %lld", &N, &M, &s, &t, &B);

	std::vector<std::vector<std::pair<ll, ll>>> G(N + 1); /* adjacency list */
	for (int i = 0; i < M; ++i) {
		ll u, v, L;
		scanf("%lld %lld %lld", &u, &v, &L);

		G[u].push_back({v, L});
	}
	/* Maximum number of skips is K */
	ll maxK = std::min(M, N - 1);
	std::vector<std::vector<ll>> dp(N + 1, std::vector<ll> (maxK + 1, INF));
	dp[s][0] = 0;

	/* Running modified Dijkstra
	 * Decision problem:
	 * 	1. Travel normally (don't skip candidate edge)
	 * 	2. Skip candidate edge (increment k)
	 */
	std::priority_queue<State, std::vector<State>, std::greater<State>> pq; // sort priority queue in ascending order 
	State initial_state = {s, 0, 0};
	pq.push(initial_state);

	while (!pq.empty()) {
		State st = pq.top();
		pq.pop();
		ll superspeeds_used = st.k;

		/* Find neighbors of current node */
		for (auto &edge : G[st.int_node]) {
			ll next = edge.first; /* neighbor */
			ll cost = edge.second;

			/* First option: don't skip edge */
			if (st.path_length + cost < dp[next][superspeeds_used]) {
				dp[next][superspeeds_used] = st.path_length + cost;
				pq.push({next, superspeeds_used, dp[next][superspeeds_used]});
			}
			/* Second option: skip edge. Don't add cost to reach the neighbor */
			if (superspeeds_used < maxK && st.path_length < dp[next][superspeeds_used + 1]) {
				dp[next][superspeeds_used + 1] = st.path_length;
				pq.push({next, superspeeds_used + 1, dp[next][superspeeds_used + 1]});
			}
		}
	}

	ll ans = -1;
	ll high = maxK;
	ll low = 0;

	while (low <= high) {
		ll mid = (low + high) / 2;
		if (dp[t][mid] <= B || dp[t][mid] >= INF) {
			ans = mid;
			high = mid - 1;
		}
		else {
			low = mid + 1;
		}
	}

	if (ans == -1) {
		printf("IMPOSSIBLE\n");
		return 0;
	}

	printf("%lld\n", ans);

	return 0;
}
