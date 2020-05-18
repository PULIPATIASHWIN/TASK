#TASK 1:
r=float(input("enter the value of r : "))
Area=3.14*r**2
print(Area)

#TASK 2:
filename=input("Input the filename : ")
index=0
for i in range(len(filename)):
    if filename[i]=='.':
       index=i
print(filename[index+1: ])

