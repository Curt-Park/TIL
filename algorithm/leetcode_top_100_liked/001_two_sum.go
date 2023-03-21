func twoSum1(nums []int, target int) []int {
    sol := make([]int, 0)
    m := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        m[nums[i]] = i
    }
    for i := 0; i < len(nums); i++ {
        if j, ok := m[target - nums[i]]; ok && i != j {
            sol = append(sol, i, j)
            break
        } 
    }
    return sol
}

func twoSum2(nums []int, target int) []int {
    m := make(map[int]int)
    for i, n := range(nums) {
        if j, ok := m[n]; ok {
            return []int{i, j}
        }
        m[target - n] = i
    }
    return []int{}
}
