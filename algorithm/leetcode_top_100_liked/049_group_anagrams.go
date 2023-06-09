package main

import (
	"sort"
	"strings"
)

func groupAnagrams1(strs []string) [][]string {
	m := map[string][]string{}
	for i := 0; i < len(strs); i++ {
		s := strings.Split(strs[i], "")
		sort.Strings(s)
		k := strings.Join(s, "")
		m[k] = append(m[k], strs[i])
	}

	ans := make([][]string, 0)
	for _, v := range m {
		ans = append(ans, v)
	}
	return ans
}

func groupAnagrams2(strs []string) [][]string {
	m := map[[26]int][]string{}
	for i := 0; i < len(strs); i++ {
		k := [26]int{}
		for _, ch := range strs[i] {
			k[ch-'a'] += 1
		}
		m[k] = append(m[k], strs[i])
	}

	ans := [][]string{}
	for _, v := range m {
		ans = append(ans, v)
	}
	return ans
}
