a = [0,0,0,0,0,
     0,0,0,6,0]

max = -1
for i in a:
    if i>max:
        max=i


count = 0;        
for i,index in enumerate(a):
    if index==max:
        print(i)
