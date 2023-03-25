func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}
	m := map[string]string{
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz",
	}
	ans := []string{""}
	for _, digit := range digits {
		next := []string{}
		for _, head := range ans {
			for _, tail := range m[string(digit)] {
				next = append(next, head+string(tail))
			}
		}
		ans = next
	}
	return ans
}

func letterCombinations(digits string) []string {
	if digits == "" {
		return []string{}
	}
	m := map[byte]string{
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
	}
	ans := []string{}
	var f func([]byte, int)
	f = func(h []byte, i int) {
		if i == len(digits) {
			ans = append(ans, string(h))
			return
		}
		for j := 0; j < len(m[digits[i]]); j++ {
			f(append(h, m[digits[i]][j]), i+1)
		}
	}
	f([]byte{}, 0)
	return ans
}
