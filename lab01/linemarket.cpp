#include <cstdio>
#include <vector>
#include <climits>
#include <algorithm>
#include <cmath>

#define ll long long

struct Interval {
	ll s;
	ll f;

	bool operator < (const Interval &other) const {
		return s < other.s; //comparing by start time
	}
};

bool isvalid(std::vector<Interval> &intervals, int N, int d) {
	ll last_pos = INT_MIN;
	ll placed = 0;

	for (ll i = 0; i < intervals.size(); ++i) {
		for (ll pos = std::max(intervals[i].s, last_pos + d); pos <= intervals[i].f; pos += d) {
			++placed;
			last_pos = pos;
			if (placed == N) {
				return true; // all N markers have been placed, so d is feasible
			}
		}
	}

	// If true was never returned after processing all intervals, return false
	return false;
}

int main () {
	ll N, M;
	scanf("%lld %lld", &N, &M);
	std::vector<Interval> intervals(M);

	for (ll i = 0; i < M; ++i) {
		scanf("%lld %lld", &intervals[i].s, &intervals[i].f);
	}

	std::sort(intervals.begin(), intervals.end()); // sort by start time, in ascending order

	ll low = 0; // minimum possible distance
	ll high = intervals.back().f - intervals.front().s; //maximum possible distance
	ll optimal = INT_MIN;

	while (low <= high) {
		ll mid = (low + high) / 2;
		if (isvalid(intervals, N, mid)) {
			optimal = mid;
			low = mid + 1;
		} else {
			high = mid - 1;
		}
	}

	if (optimal == INT_MIN)
		return 0;

	printf("%lld\n", optimal);
	return 0;
}
