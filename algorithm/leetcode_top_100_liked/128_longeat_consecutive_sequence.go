package main

func longestConsecutive(nums []int) int {
	m := map[int]bool{}
	for _, n := range nums {
		m[n] = true
	}
	maxCnt := 0
	for n, _ := range m {
		_, existPre := m[n-1]
		cnt := 0
		for !existPre {
			if _, exist := m[n]; !exist {
				break
			}
			cnt, n = cnt+1, n+1
		}
		if maxCnt < cnt {
			maxCnt = cnt
		}
	}
	return maxCnt
}
