package main

func minWindow(s string, t string) string {
	tgtCnt := map[byte]int{}
	srcCnt := map[byte]int{}
	for i := 0; i < len(t); i++ {
		if _, exist := tgtCnt[t[i]]; !exist {
			srcCnt[t[i]], tgtCnt[t[i]] = 0, 1
		} else {
			tgtCnt[t[i]] += 1
		}
	}
	l, cnt, size, ans := 0, 0, len(s)+1, ""
	for r := 0; r < len(s); r++ {
		if _, exist := srcCnt[s[r]]; !exist {
			continue
		}
		srcCnt[s[r]] += 1
		if srcCnt[s[r]] == tgtCnt[s[r]] {
			cnt += 1
		}
		for l <= r {
			if _, exist := srcCnt[s[l]]; exist {
				if srcCnt[s[l]] <= tgtCnt[s[l]] {
					break
				}
				srcCnt[s[l]] -= 1
			}
			l += 1
		}
		if cnt == len(tgtCnt) && size > r-l+1 {
			size = r - l + 1
			ans = s[l : r+1]
		}
	}
	if size == len(s)+1 {
		return ""
	}
	return ans
}
