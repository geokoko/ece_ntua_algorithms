#include <cstdio>
#include <vector>
#include <utility>
#include <limits>
#include <queue>
#include <iostream>
#include <cstring>

#define ll long long
#define INF 1000000000000LL

static ll dp[1100][1100]; // tracking the (node, k) state shortest_paths here. 

/*  int_node   = current node
 *  k          = edges skipped so far
 *  path_length= the total distance traveled so far
 */
struct State {
	ll int_node;
	ll k;
	ll path_length;
};

/* Custom comparator for the priority queue:
 * Sort by smaller k and then 
 * prioritize smaller path length
 */

struct CompareState {
	inline bool operator()(const State &a, const State &b) const {
		if (a.k != b.k) {
			return a.k > b.k;  // prioritize smaller k
		}
		return a.path_length > b.path_length;  // then prioritize smaller path_length
	}
};

int main () {
	int N, M, s, t;
	ll B;
	scanf("%d %d %d %d %lld", &N, &M, &s, &t, &B);

	std::vector<std::vector<std::pair<ll, ll>>> G(N + 1);
	G.reserve(N + 1);

	for (int i = 0; i < M; ++i) {
		int u, v;
		ll L;
		scanf("%d %d %lld", &u, &v, &L);
		G[u].push_back({v, L});
	}

	int maxK = std::min(M, N - 1);
	memset(dp, 0x3f, sizeof(dp));
	dp[s][0] = 0LL;

	/* pop the state with the fewest skips, then smallest path_length first. */
	std::priority_queue<State, std::vector<State>, CompareState> pq;
	pq.push({(ll)s, 0LL, 0LL});

	bool found = false;

	while (!pq.empty()) {
		State st = pq.top();
		pq.pop();

		ll node      = st.int_node;
		ll usedSkips = st.k;
		ll dist      = st.path_length;

		/* Skip if this state is outdated */
		if (dist > dp[node][usedSkips]) {
			continue;
		}

		/* If we've reached t with dist <= B, we have the minimum skips, as we prioritize the smaller k. When we encounter a valid solution, we know that k is
		 * minimal.
		 */
		if (node == t && dist <= B) {
			printf("%lld\n", usedSkips);
			found = true;
			break;
		}

		/* If we already exceed the budget B, no need to explore further */
		if (dist > B) {
			continue;
		}

		/* Explore neighbors of the current node */
		for (auto &edge : G[node]) {
			ll nxt  = edge.first;
			ll cost = edge.second;

			/* Option 1: Travel normally (no skip) */
			ll ndist = dist + cost;
			if (ndist < dp[nxt][usedSkips]) {
				dp[nxt][usedSkips] = ndist;
				pq.push({nxt, usedSkips, ndist});
			}

			/* Option 2: Skip this edge */
			if (usedSkips < maxK) {
				ll ndistSkip = dist;  // cost = 0
				ll newK = usedSkips + 1;
				if (ndistSkip < dp[nxt][newK]) {
					dp[nxt][newK] = ndistSkip;
					pq.push({nxt, newK, ndistSkip});
				}
			}
		}
	}

	if (!found) {
		printf("IMPOSSIBLE\n");
	}

	return 0;
}

