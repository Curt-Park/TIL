package main

func partition(s string) [][]string {
	ans := [][]string{}
	m := map[[2]int]bool{}
	palindromes := []string{}
	var find func(l, r int)
	find = func(begin int, end int) {
		if begin == len(s) && len(palindromes) > 0 {
			cpy := make([]string, len(palindromes))
			copy(cpy, palindromes)
			ans = append(ans, cpy)
		}
		exist := false
		if _, exist = m[[2]int{begin, end}]; !exist {
			substring := s[begin:end]
			exist = isPalindrome(substring)
		}
		if exist {
			m[[2]int{begin, end}] = true
			palindromes = append(palindromes, s[begin:end])
			for i := end; i <= len(s); i++ {
				find(end, i)
			}
			palindromes = palindromes[:len(palindromes)-1]
		}
	}
	for i := 0; i <= len(s); i++ {
		find(0, i)
	}
	return ans
}

func isPalindrome(s string) bool {
	if len(s) == 0 {
		return false
	}
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-i-1] {
			return false
		}
	}
	return true
}
