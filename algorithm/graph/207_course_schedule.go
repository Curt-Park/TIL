package main

func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := make(map[int][]int, numCourses)
	for _, adj := range prerequisites {
		from, to := adj[0], adj[1]
		graph[from] = append(graph[from], to)
	}
	states := make([]int, numCourses)
	var isCyclic func(int) bool
	isCyclic = func(val int) bool {
		if states[val] == 2 { // not cyclic
			return false
		}
		if states[val] == 1 { // cyclic
			return true
		}
		states[val] = 1
		for _, next := range graph[val] {
			if isCyclic(next) {
				return true
			}
		}
		states[val] = 2
		return false
	}
	for i := 0; i < numCourses; i++ {
		if isCyclic(i) {
			return false
		}
	}
	return true
}
