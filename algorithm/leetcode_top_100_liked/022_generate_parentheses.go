func generateParenthesis(n int) []string {
	ans := []string{}
	var f func([]byte, int, int)
	f = func(h []byte, l int, r int) {
		if l == 0 && r == 1 {
			ans = append(ans, string(append(h, ')')))
			return
		}
		if l > 0 {
			f(append(h, '('), l-1, r)
		}
		if r > 0 && l < r {
			f(append(h, ')'), l, r-1)
		}
	}
	f([]byte{'('}, n-1, n)
	return ans
}
