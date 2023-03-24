package main

func longestCommonPrefix(strs []string) string {
	ans := []byte{}
	for i := 0; i < len(strs[0]); i++ {
		for _, str := range strs {
			if i == len(str) || strs[0][i] != str[i] {
				return string(ans)
			}
		}
		ans = append(ans, strs[0][i])
	}
	return string(ans)
}
