func longestValidParentheses(s string) int {
	stack, flag, cnt, ans := []int{}, make([]int, len(s)), 0, 0
	for i, ch := range s {
		if ch == '(' {
			stack = append(stack, i)
		} else if len(stack) > 0 {
			open := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			flag[open], flag[i] = 1, 1
		}
	}
	for i := 0; i < len(flag); i++ {
		cnt = (cnt + flag[i]) * flag[i]
		if ans < cnt {
			ans = cnt
		}
	}
	return ans
}
