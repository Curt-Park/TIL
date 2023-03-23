func longestPalindrome(s string) string {
	ansL, ansR := 0, 0

	checkPalindrome := func(l, r int) (int, int) {
		for l >= 0 && r < len(s) && s[l] == s[r] {
			l, r = l-1, r+1
		}
		return l + 1, r - 1
	}

	for i := 0; i < len(s); i += 1 {
		l1, r1 := checkPalindrome(i-1, i+1)
		l2, r2 := checkPalindrome(i, i+1)

		l, r := l1, r1
		if r-l+1 < r2-l2+1 {
			l, r = l2, r2
		}
		if ansR-ansL+1 < r-l+1 {
			ansL, ansR = l, r
		}
	}
	return string(s[ansL : ansR+1])
}
