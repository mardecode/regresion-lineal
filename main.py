import csv
import numpy as np
import matplotlib.pyplot as plt

plt.ion()



#VARIABLES GLOBALES *******************************************************************************
x = []
y = []
h=[]
n= 2 # numero de dimensiones
thetas  = np.random.rand(n)
#thetas = [-4,1]
print "thetas aleatorios " ,thetas
alpha = np.ones(n)
error = []
errorF = 0
countDatos = 0
dNormal = []
dTemporal = []

#Fin declaracin de variables *********************************************************************

#atom://teletype/portal/624d3220-1890-4824-b17b-97f0fdd835f0
#FUNCIONES ***************************************************************************************
def getH():
    global h
    h = np.matmul(x,thetas)


def getError(): #NoSquare
    global error
    error = y-h

def getDerivadas(b):
    global dTemporal
    global dNormal

    arrayDerivadas = []
    for i in range(n):
        arrayDerivadas.append(float((alpha[i]*error*-x[:,i]).sum())/float(countDatos))
    if b:
        dNormal = np.array(arrayDerivadas)
    else:
        dTemporal = np.array(arrayDerivadas)

def getDerivada(i):
    return float((alpha[i]*error*-x[:,i]).sum())/float(countDatos)

def changeThetas():
    global thetas
    global dTemporal
    global alpha

    for i in range(n):
        thetas[i] = thetas[i]-dNormal[i]
        getH()
        getError()
        getDerivadas(1)#derivada normal cambiar todo

        newDerivada = dNormal[i]
        a= 0
        while (abs(newDerivada)>abs(dTemporal[i]) and abs(newDerivada)>0.001):
            print abs(newDerivada)," > ",abs(dTemporal[i])
            a =a+1
            if(a>10):
                break
            print a
            print "alpha de i",alpha[i]
            print "entre 2",alpha[i]/2
            alpha[i]=alpha[i]/2
            newDerivada = getDerivada(i)
        dTemporal[i] = newDerivada
    #    print "derivada dTemporal ",dTemporal
        print "alphas ",alpha
        print "thetas " ,thetas

def promedio(arreglo):
    return np.absolute(arreglo).sum()/n

def getErrorF():
    global errorF
    errorF =  np.power(errorF,2).sum()/(2*countDatos)



#leyendo archivo *********************************************************
with open('datos4.csv', 'rb') as csvfile:
    datos = csv.reader(csvfile, delimiter=',')
    for row in datos:
#        for i in len(row):
            x.append([1,float(row[0])])
        y.append(float(row[1]))
        countDatos += 1

x = np.array(x)
y = np.array(y)
# fin leer archivo **********************************************************

### ALGORITMO ####
getH()
getError()
getDerivadas(1)
getDerivadas(0)
plox = 0
print "d Temp ",dTemporal, "promedio: ", promedio(dNormal)
while(promedio(dNormal) >= 0.01):
    print "***************************************************++"
    changeThetas()
    plox +=1
    #print "plox ", plox, thetas
    if(plox==100):
        break
    print "d Temp ",dNormal, "promedio: ", promedio(dNormal)

    plt.scatter(x[:,1],y)
    plt.axis([-120, 160, -40, 130])
    plt.plot([-120,160],[thetas[0]+thetas[1]*-120 , thetas[0]+thetas[1]*160])
    plt.savefig('fig'+str(plox))
    plt.pause(0.01)

while True:
    plt.pause(0.01)

'''
#funcion hallar h(x) = theta[0] + theta[1]*x
def h(x,theta):
    return np.matmul(x,theta)
#calculano el valor del error promedio
def error(y,h):
    return y-h
def errorS(error):
    return np.power(error,2).sum()/(2*countDatos)

factores = [1,1]
derivadas =
def nuevoTheta(i,c):
    float( (c*error*(-1)).sum())/float(countDatos)
    return nuevo

#cambiando thetas
def changeThetas(error,x,c1,c2):
#    print "error ",error
    for i in range(thetas.size):
        thetas[i] = thetas[i]-nuevoTheta(i,factores[i])

    thetas[0] = thetas[0] - float( (c1*error*(-1)).sum())/float(countDatos)
    print "new theta [0] | ",thetas[0]

    thetas[1] = thetas[1] - float((c2*np.multiply(error,-x[:,1])).sum())  / float(countDatos)
    print "new theta [1] |",thetas[1]
    return thetas

he = h(x,thetas)
#print "thetas aleatorios ",thetas
#print h
e = error(y,he)
err = errorS(e)
asdf = 0
while err > 0.4:
    if asdf==500:
        break
    thetas = changeThetas(e,x,0.1,0.001)
    he = h(x,thetas)
    e = error(y,he)
    err = errorS(e)
    print "error ", err
    asdf += 1
    plt.scatter(x[:,1],y)
    plt.axis([-120, 160, -40, 130])
    plt.plot([-120,160],[thetas[0]+thetas[1]*-120 , thetas[0]+thetas[1]*160])

    plt.pause(0.01)
    #plt.clf()


while True:
    plt.pause(0.01)

#ha = h(x,thetas)

#print error(y,ha)

#Holi ya estoy aqui >___< .. y te amo!
#holi yo tambien te amo :P
#No te enojes conmigo u.U
# no me hagas enojar
'''
