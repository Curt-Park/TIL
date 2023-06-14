package main

func climbStairs(n int) int {
	m := map[int]int{}
	m[-1], m[0] = 0, 1
	var find func(int) int
	find = func(n int) int {
		if _, exists := m[n]; exists {
			return m[n]
		}
		m[n] = find(n-1) + find(n-2)
		return m[n]
	}
	return find(n)
}
