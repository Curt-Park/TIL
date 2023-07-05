package main

func wordBreak(s string, wordDict []string) bool {
	m, dp := map[string]bool{}, map[string]bool{}
	for _, word := range wordDict {
		m[word] = true
	}
	dp[""] = true
	var find func(string) bool
	find = func(s string) bool {
		if _, exist := dp[s]; exist {
			return dp[s]
		}
		res := false
		for i := 1; i <= len(s); i++ {
			sub := s[:i]
			if _, exist := m[sub]; !exist {
				continue
			}
			res = res || find(s[i:])
			if res {
				break
			}
		}
		dp[s] = res
		return res
	}
	return find(s)
}
