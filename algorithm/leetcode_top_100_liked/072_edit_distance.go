package main

func minDistance1(word1 string, word2 string) int {
	m := make([]int, len(word1)+1)
	for i := 0; i <= len(word1); i++ {
		m[i] = i
	}
	var prev int
	for i := 1; i <= len(word2); i++ {
		prev, m[0] = m[0], i
		for j := 1; j <= len(word1); j++ {
			var next int
			if word2[i-1] == word1[j-1] {
				next = prev
			} else {
				next = min(min(prev, m[j-1]), m[j]) + 1
			}
			prev, m[j] = m[j], next
		}
	}
	return m[len(word1)]
}

func minDistance2(word1 string, word2 string) int {
	m := map[[2]int]int{}
	var find func(int, int) int
	find = func(idx1, idx2 int) int {
		if idx1 == 0 {
			return idx2
		}
		if idx2 == 0 {
			return idx1
		}
		if _, exists := m[[2]int{idx1, idx2}]; exists {
			return m[[2]int{idx1, idx2}]
		}
		if word1[idx1-1] == word2[idx2-1] {
			return find(idx1-1, idx2-1)
		}
		ins := find(idx1, idx2-1)
		del := find(idx1-1, idx2)
		rep := find(idx1-1, idx2-1)
		m[[2]int{idx1, idx2}] = min(min(ins, del), rep) + 1
		return m[[2]int{idx1, idx2}]
	}
	return find(len(word1), len(word2))
}
