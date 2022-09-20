#Author: @sevilayerkan
#Date: 20.09.22

#This solution is version of https://projecteuler.net/problem=42 problem for HackerRank 
#Question source: https://www.hackerrank.com/contests/projecteuler/challenges/euler042/problem

import math as m
    
#Find positive triangular root of num with using formula
#Formula resource : https://en.wikipedia.org/wiki/Triangular_number
def reverseTri(num):
    result = (m.sqrt(num * 8 + 1) - 1) / 2
    return result


testCase = int(input()) #Takes test case number
for i in range(0,testCase):
    number = int(input())
    result = reverseTri(number)
    if result == int(result) :
        print(int(result))
    else:
        print("-1")
    