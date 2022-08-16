//Author: @sevilayerkan
//Date: 16.08.2022
//Problem case: Find the sum of all the primes below two million.

package main

import (
	"fmt"
	"math"
)

const twoMillion = 2000000

func main() {

	fmt.Println(sumPrimes(twoMillion))

}

// For checking number is prime
func isPrime(num int) bool {
	var sqt = math.Sqrt(float64(num))
	if num >= 2 {
		for i := 2; i <= int(sqt); i++ {
			if num%i == 0 {
				return false
			}

		}
	}
	return true
}

// Calculates sum of primes in number
func sumPrimes(num int) int {
	sum := 0
	for i := 2; i < num; i++ {
		if isPrime(i) {
			sum += i
		}
	}
	return sum
}
