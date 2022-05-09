import math
def minEnergy(heights):
    minimum = 0
    n = len(heights)
    for i in range(n-1,-1,-1):
        minimum = math.ceil((heights[i]+minimum)/2)
    return minimum


if __name__ == '__main__':
    first_input = int(input().strip())
    heights = list(map(int,input().rstrip().split()))[:first_input]
    print("{}".format(minEnergy(heights)))


