def bpair(a,b):
	n=0
	for i in a:
		if i in b:
			b.remove(i) #remove the index to keep it disjoint disjoint 
			n+=1
	if n<len(a):
		return n+1
	else:
		return n-1 
	
	
if __name__ == '__main__':
	n = int(input()) #input length
	
	'''Taking input of length n'''
	a = list(map(int, input().rstrip().split()))[:n]
	b = list(map(int, input().rstrip().split()))[:n]
	print("{}".format(bpair(a,b)))
	