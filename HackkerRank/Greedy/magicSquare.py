def isMountain(s):
    if (len(s)<3):
        return False
    i = 1
    while(i<len(s) and s[i-1]< s[i+1]):
        i+=1
    if(i==1 or i==len(s)):
        return False
    while(i<= len(s) and s[i-1]>s[i]):
        i+=1
    
    return i == len(s)
    

if __name__ == '__main__':
    s = list(map(int,input().rstrip().split()))
    print(s)
    print(isMountain(s))

