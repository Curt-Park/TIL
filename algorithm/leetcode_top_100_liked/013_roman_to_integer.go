package main

import "fmt"

func romanToInt(s string) int {
	ans, i := 0, 0
	m := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	for i < len(s) {
		if i < len(s)-1 && m[s[i]] < m[s[i+1]] {
			ans += m[s[i+1]] - m[s[i]]
			i += 1
		} else {
			ans += m[s[i]]
		}
		i += 1
	}
	return ans
}

func main() {
	fmt.Println(romanToInt("III"))
	fmt.Println(romanToInt("MCMXCIV"))
}
