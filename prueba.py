import numpy as np
y = [[1,2],[9,0],[5,10]]
x = [1,99]
x.append(10)
y.append(x)
z= []
for i in range (0,len(x)-1):
    z.append(x[i])
    print i

w =[]
w.append(x[len(x)-1])
print z
print w
#y = np.array(y)
#ymax = np.amax(y)

#print y
