#Author: @sevilayerkan
#Date: 5.08.22

#Find the nth pentagonal number
def nthPentagonal(n):
    return n*(3*n-1)/2

#Find Pj and Pk for given D
def findPjPk(D):
    for j in range(1,1000):
        for k in range(j+1,1000):
            if nthPentagonal(j)+nthPentagonal(k)==D:
                return j,k
    return None

#Find D for given Pj and Pk
def findD(Pj,Pk):
    return abs(Pk-Pj)   
    #abs() function returns the absolute value of the number

#Main function
if __name__ == "__main__":
    print(findD(findPjPk(1000)))
    #Returns 5482660