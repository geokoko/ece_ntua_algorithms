#include <cstdio>
#include <vector>  
#include <algorithm>  
#include <climits>  
#include <iostream>  
#include <cmath>  
  
#define ll long long
#define EPS 1e-8
  
struct Edge {  
    ll u, v, p, w;  
    double cost;  
  
    Edge(ll u, ll v, ll p, ll w) : u(u), v(v), p(p), w(w), cost(0.0) {}  
  
    bool operator < (const Edge& e) const {  
        return cost - e.cost > EPS;  
    }  
};  
  
/* 
 * Union-Find Disjoint Set 
 * make_set(n): create n sets 
 * find(u): find the set that contains u 
 * unite(u, v): unite the sets that contain u and v 
 */  
  
std::vector<ll> parent, rank;  
  
void make_set(ll n) {  
    parent.resize(n);  
    rank.resize(n, 0);  
    for (ll i = 0; i < n; ++i)  
        parent[i] = i;  
}  
  
ll find(ll u) {  
    if (parent[u] != u)  
        parent[u] = find(parent[u]);  
    return parent[u];  
}  
  
bool unite(ll u, ll v) {  
    ll pu = find(u);  
    ll pv = find(v);  
    if (pu == pv)  
        return false;  
    if (rank[pu] < rank[pv])  
        parent[pu] = pv;  
    else {  
        parent[pv] = pu;  
        if (rank[pu] == rank[pv])  
            rank[pu]++;  
    }  
    return true;  
}  
  
/* 
 * Kruskal's algorithm 
 * isPossible(R, edges, N, sum_w, sum_p): check if it is possible to construct a MST with R 
 * and return the sum of weights and profits 
 */  
  
bool isPossible (double R, std::vector<Edge>& edges, ll N, ll &sum_w, ll &sum_p, double &total_c) {  
    std::sort(edges.begin(), edges.end());  
  
    make_set(N);  
    total_c = 0.0;  
    ll edges_used = 0;  
    ll temp_sum_w = 0, temp_sum_p = 0;  
  
    for (auto& edge : edges) {  
        if (unite(edge.u, edge.v)) {  
            total_c += edge.cost;  
            temp_sum_w += edge.w;  
            temp_sum_p += edge.p;  
            edges_used++;  
            if (edges_used == N - 1)  
                break;  
        }  
    }  
  
    //is it MST?  
    if (edges_used != N - 1) {  
        return false;  
    }  
  
    if (total_c >= -EPS) {  
        sum_w = temp_sum_w;  
        sum_p = temp_sum_p;  
        return true;  
    }  
  
    return false;  
}  
  
int main() {  
    std::ios::sync_with_stdio(false);  
    std::cin.tie(nullptr);  
  
    ll N, M;  
    scanf("%lld %lld", &N, &M);  
    std::vector<Edge> edges;  
  
    for (ll i = 0; i < M; i++) {  
        ll u, v, p, w;  
        scanf("%lld %lld %lld %lld", &u, &v, &p, &w);  
        edges.emplace_back(Edge{u - 1, v - 1, p, w});  
    }  
  
	double low = 0.0;  
    double high = 1e9;  
    ll s_p = 0, s_w = 0;  
  
    while (high - low > EPS) {  
        double mid = (low + high) / 2.0;
		double total_c = 0.0;
		ll temp_s_p = 0, temp_s_w = 0;
  
        for (auto& edge : edges) {  
            edge.cost = edge.p - mid * edge.w;  
        }  
  
        if (isPossible(mid, edges, N, temp_s_p, temp_s_w, total_c)) {  
            s_p = temp_s_p;
        	s_w = temp_s_w;
			low = mid;  
        }  
        else {  
            high = mid;  
        }  
    }  
  
    printf("%lld %lld\n", s_w/std::__gcd(s_p, s_w), s_p/std::__gcd(s_p, s_w));  
  
    return 0;  
}   
