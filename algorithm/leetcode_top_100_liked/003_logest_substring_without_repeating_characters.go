func lengthOfLongestSubstring(s string) int {
	m := make(map[string]int)
	ans, l := 0, 0
	for i, ch := range s {
		if j, ok := m[string(ch)]; ok && j >= l {
			l = j + 1
		}
		m[string(ch)] = i
		if ans < i-l+1 {
			ans = i - l + 1
		}
	}
	return ans
}
