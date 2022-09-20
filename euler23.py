#Author: @sevilayerkan
#Date: 20.09.22

#TO-DO : 1) Needs refactoring, 2) Should be solved with different approach
#This solution is version of https://projecteuler.net/problem=23 problem for HackerRank
#Question source: https://www.hackerrank.com/contests/projecteuler/challenges/euler023/problem

def abundant(n):
    n1 = int(n**(1/2))+1
    tot = 0
    for i in range(2, n1):
        if (n % i == 0):
            if (i != n/i):
                tot += i+(n/i)
            else:
                tot += i
    if (n < tot+1):
        return (True)
    else:
        return (False)


num = int(input())
for i in range(num):
    n = int(input())
    flag = 0
    for i in range(2, int(n/2)+1):
        if (abundant(i) and abundant(n-i)):
            print("YES")
            flag = 1
            break
    if (flag == 0):
        print("NO")
