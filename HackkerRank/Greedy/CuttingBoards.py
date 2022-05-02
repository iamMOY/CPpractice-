def cutCost(cost_x,cost_y):
	
	hs=1
	vs=1 
	cost=0 #cost of sampling
	
	cost_x.sort(reverse=True)
	cost_y.sort(reverse=True)
	m=len(cost_x)
	n=len(cost_y)


	while(hs!=(m+1) and vs!= (n+1)):

		if((cost_x[0] >= cost_y[0])):
			cost += (cost_x[0]*vs)%(10**9+7)
			hs+=1
			cost_x.pop(0)
			
		else:
			cost += (cost_y[0]*hs)%(10**9+7)
			vs+=1
			cost_y.pop(0)
		
	while(hs<m+1):
		cost+=(cost_x[0]*vs)%(10**9+7)
		hs+=1
		cost_x.pop(0)
	while(vs<n+1):
		cost+=(cost_y[0]*hs)%(10**9+7)
		vs+=1
		cost_y.pop(0)
		
	

	return cost
	

if __name__ == "__main__":
	q = int(input().strip()) #number of querries
	for i in range(q):
		''' taking mxn inputs '''
		inputs = input().rstrip().split()
		m = int(inputs[0]) 
		n = int(inputs[1]) 
		''' Horizontal cost (cost_x) vertical cost (cost_y) '''
		cost_x = list(map(int,input().rstrip().split()))
		cost_y = list(map(int,input().rstrip().split()))
		print("{}\n".format(cutCost(cost_x,cost_y)))
		

