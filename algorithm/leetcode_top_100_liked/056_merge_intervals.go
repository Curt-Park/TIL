package main

import "sort"

func merge(intervals [][]int) [][]int {
	ans := [][]int{}
	sort.Sort(Items(intervals))

	interval := intervals[0]
	for i := 1; i < len(intervals); i++ {
		newInterval := []int{}
		if interval[0] <= intervals[i][0] && intervals[i][0] <= interval[1] {
			newInterval = append(newInterval, interval[0])
			newInterval = append(newInterval, max(interval[1], intervals[i][1]))
			interval = newInterval
		} else {
			ans = append(ans, interval)
			interval = intervals[i]
		}
	}
	ans = append(ans, interval)
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

type Items [][]int

func (items Items) Less(i, j int) bool {
	if items[i][0] < items[j][0] {
		return true
	}
	if items[i][0] == items[j][0] && items[i][1] < items[j][1] {
		return true
	}
	return false
}

func (items Items) Swap(i, j int) {
	items[i], items[j] = items[j], items[i]
}

func (items Items) Len() int {
	return len(items)
}
