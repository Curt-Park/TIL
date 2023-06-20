package main

import "math"

func maxProfit(prices []int) int {
	min, maxProfit := math.MaxInt, 0
	for _, price := range prices {
		if min > price {
			min = price
		}
		if maxProfit < price-min {
			maxProfit = price - min
		}
	}
	return maxProfit
}
