f = open("Use Case1- triangle_test_4rows.txt","r")
l1 = []
final = []
l = f.readlines()
print("Input taken from files")
print(l)
for i in l:
    s = i.split()
    l1.append(s)
print("after splitting the files into individual numbers")
print(l1)
for i in l1:
    x = i
    for i in range(len(x)):
        x[i] = int(x[i])
    final.append(x)
max_length = 0
for i in final:
    if(len(i)>max_length):
        max_length = len(i)
for i in final:
    x = max_length-len(i)
    for j in range(x):
        i.append(0)
for i in range(max_length-2,-1,-1):
    for j in range(0,i+1):
        if(final[i+1][j]>final[i+1][j+1]):
            final[i][j]+=final[i+1][j]
        else:
            final[i][j]+=final[i+1][j+1]
print("Maximum weight is : ",end = "")
print(final[0][0])
        
    
