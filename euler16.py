#Author: @sevilayerkan
#Date: 15.09.22

#This solution is version of https://projecteuler.net/problem=16 problem for HackerRank
#Question source: https://www.hackerrank.com/contests/projecteuler/challenges/euler016/problem
#Problem case: What is the sum of the digits of the number 2^N

#Finds sum of digits of any given integer
def sumDigits(num):
    total = 0
    while (num > 0):
        total += (num % 10)
        num = int(num // 10)
    return total


testCaseSize = int(input())

for i in range(0, int(testCaseSize)):
    number = int(input())
    result = int(pow(2, int(number)))
    print(sumDigits(result))
