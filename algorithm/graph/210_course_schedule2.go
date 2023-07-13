package main

func findOrder(numCourses int, prerequisites [][]int) []int {
	graph := make(map[int][]int, numCourses)
	for _, edge := range prerequisites {
		graph[edge[0]] = append(graph[edge[0]], edge[1])
	}
	result := []int{}
	states := make([]int, numCourses)
	var dfs func(int) bool
	dfs = func(node int) bool {
		if states[node] == 2 {
			return false
		}
		if states[node] == 1 {
			return true
		}
		states[node] = 1
		for _, adj := range graph[node] {
			if dfs(adj) {
				return true
			}
		}
		states[node] = 2
		result = append(result, node)
		return false
	}
	for i := 0; i < numCourses; i++ {
		if dfs(i) {
			return []int{}
		}
	}
	return result
}
