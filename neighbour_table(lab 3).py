import math
import random

def calculate_distance(node1,node2):
    return round(math.sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2),4)

num_nodes=10
area_size=500

nodes,l=[],[]
for i in range(1,11):
    x=random.randint(0,50)
    y=random.randint(0,10)
    nodes.append([x,y])
    print("Node",i,"x-axis:",x)
    print("Node",i,"y-axis:",y)
for i in range(num_nodes):
    l1=[]
    for j in range(num_nodes):
        distance=calculate_distance(nodes[i],nodes[j])
        l1.append(distance)
    l.append(l1)
    
print("Distance table")
print("{:<10} {}".format(""," ".join(f"{f'Node{i}':<10}" for i in range(1,num_nodes+1))))
for i in range (1,len(l)+1):
    print(f"Node{i}:",end=" ")
    for j in range(len(l[i-1])):
        distance=l[i-1][j] 
        print(f'{distance:<10}',end=" ")
    print('\n') 
    
dist=float(input("Enter the range limit for the nodes:"))
print("Neighbour Table")
for i in range(len(l)):
    node=[]
    for j in range(len(l[i])):
        if l[i][j]<=dist and i!=j:
            node.append(j+1)
    print("Neighbours of node",i+1,"is:",end=" ")
    
    if len(node)!=0:
        for k in node:
            print(k,end=" ")
        print()
    else:
            print("No neighbours in this range")
