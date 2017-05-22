a,b,c=map(int,input().split())
trunk=[[] for i in range(a)]
for j in range(b):
	d,e=map(int,input().split())
	trunk[d-1].append(e)
	trunk[e-1].append(d)
trunk=list(map(sorted,trunk))
visited=[c]
history=[c]
cursor=0
while len(history)!=0:
	moved=False
	x=trunk[history[-1]-1]
	for k in range(len(x)):
		if x[k] not in visited:
			moved=True
			visited.append(x[k])
			history.append(x[k])
			break
	if not moved:
		history.pop()
print(" ".join(map(str,visited)))
visited=[c]
queue=[c]
while len(queue)!=0:
	x=queue.pop(0)
	for l in range(len(trunk[x-1])):
		if trunk[x-1][l] not in visited:
			queue.append(trunk[x-1][l])
			visited.append(trunk[x-1][l])
print(" ".join(map(str,visited)))