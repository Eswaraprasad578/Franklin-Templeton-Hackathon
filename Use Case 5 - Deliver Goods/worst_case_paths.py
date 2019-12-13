from itertools import permutations as p
n = int(input())
list_of_permutations = p(list(range(1,n+1)))
l = []
for i in list_of_permutations:
    l.append(list(i))
import math
print("Maximum distance is : ",((n*(n-1))//2)+n//2-1)
print("All possible paths of maximum distance")
for i in l:
    s = 0
    for j in range(0,len(i)-1):
        s+=math.fabs(i[j]-i[j+1])
    if(s==(((n*(n-1))//2)+n//2-1)):
        print(i)
