def getMinimumCost(k,c):
    cost = 0
    c.sort(reverse=True)
    for i in range(0,len(c)):
        cost = cost + (i//k + 1)*c[i]
    return cost

if __name__ == "__main__":
    nk = input().split()
    n = int(nk[0]) #number of flowers
    k = int(nk[1]) #number of friends
    c = list(map(int, input().rstrip().split())) #cost of flowers
    minimumCost = getMinimumCost(k, c)
    print("{}".format(minimumCost))


