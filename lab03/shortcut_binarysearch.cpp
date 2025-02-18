#include <cstdio>  
#include <vector>  
#include <utility>  
#include <limits>  
#include <queue>  
#include <iostream>
#include <cstring>

#define ll long long  
#define INF 1000000000000LL

static ll dp[1100][1100];

struct State {  
	ll int_node;    /* current node */  
	ll k;           /* how many edges have we skipped with superspeed */  
	ll path_length; /* path length */  

	inline bool operator > (const State& other) const {  
		return path_length > other.path_length;  
	}     
};  

inline bool isReachable(int N, int s, int t, ll B, const std::vector<std::vector<std::pair<ll, ll>>>& G, ll mid) {    
	// Initialize dp with INF   
        memset(dp, 0x3f, sizeof(dp)); 
	dp[s][0] = 0;

	/* Running modified Dijkstra 
	 * Decision problem: 
	 *  1. Travel normally (don't skip candidate edge) 
	 *  2. Skip candidate edge (increment k) 
	 * Optimization idea: 
	 *  Since dp[n][k] >= dp[n][k + 1] for all k, we can binary search over k to check each time whether we can reach destination 
	 *  with at most K steps. If yes, search for a smaller k. If no, search for a higher value of k. 
	 */  

	std::priority_queue<State, std::vector<State>, std::greater<State>> pq; // sort priority queue in ascending order   
	State initial_state = {s, 0, 0LL};  
	pq.push(initial_state);  

	while (!pq.empty()) {  
		State st = pq.top();  
		pq.pop();  

		ll node      = st.int_node;  
		ll usedSkips = st.k;  
		ll dist      = st.path_length;  

		/* Skip outdated states. */  
		if (dist > dp[node][usedSkips])  
			continue;  

		if (node == t && dist <= B) {  
			return true;  
		}  

		if (dist > B)  
			continue;  

		/* Find neighbors of current node */  
		for (const auto &edge : G[node]) {  
			ll nxt = edge.first; /* neighbor */  
			ll cost = edge.second;  

			/* First option: don't skip edge */  
			ll ndist = dist + cost;  
			if (ndist <= B && ndist < dp[nxt][usedSkips]) {  
				dp[nxt][usedSkips] = ndist;  
				pq.push({nxt, usedSkips, ndist});  
			}  

			/* Second option: skip edge. Don't add cost to reach the neighbor */  
			if (usedSkips < mid) {  
				// cost = 0 for skipping  
				if (dist < dp[nxt][usedSkips + 1]) {  
					dp[nxt][usedSkips + 1] = dist;  
					pq.push({nxt, usedSkips + 1, dist});  
				}  
			}  
		}  
	}  

	for (ll k = 0; k <= mid; ++k) {  
		if (dp[t][k] <= B)  
			return true;  
	}  
	return false;  
}  

int main () {  
	int N, M, s, t;
	ll B;
	scanf("%d %d %d %d %lld", &N, &M, &s, &t, &B);  

	std::vector<std::vector<std::pair<ll, ll>>> G(N + 1); /* adjacency list */  
	G.reserve(N + 1);  

	for (int i = 0; i < M; ++i) {  
		int u, v, L;  
		scanf("%d %d %d", &u, &v, &L);  

		G[u].emplace_back(v, L);  
	}  
	/* Maximum number of skips is K */  
	int maxK = std::min(M, N - 1);  

	int ans = -1;  
	int high = maxK;  
	int low = 0;  

	while (low <= high) {  
		ll mid = (low + high) / 2;  
		if (isReachable(N, s, t, B, G, mid)) {  
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

	printf("%d\n", ans);  

	return 0;  
}  

