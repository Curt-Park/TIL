func twoSum(nums []int, target int) []int {
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
