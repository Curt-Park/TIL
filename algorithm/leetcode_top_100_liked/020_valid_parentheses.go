func isValid(s string) bool {
	m := map[rune]rune{')': '(', '}': '{', ']': '['}
	stack := []rune{}
	for _, ch := range s {
		if _, ok := m[ch]; !ok { // "({["
			stack = append(stack, ch)
		} else if len(stack) != 0 && stack[len(stack)-1] == m[ch] {
			stack = stack[:len(stack)-1]
		} else {
			return false
		}
	}
	return len(stack) == 0
}
