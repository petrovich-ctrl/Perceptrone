import numpy as np

center=[2.0,2.5]
r=3.9
epsilon=10**(-3)


def check_circle(x,a,r, epsilon):
    if ((x[0]-a[0])**2)+((x[1]-a[1])**2)>(r**2)+epsilon:
        return 0
    elif ((x[0]-a[0])**2)+((x[1]-a[1])**2)<(r**2)-epsilon:
        return 1
    else :
        return -1


def generate(a1,a2,a3,a4,amount):
    x0=np.array([[0.0,0.0,1.0,0.0]])
    x_coor = np.array([(np.random.rand()*(a2 - a1) + a1) for i in range(amount)])
    y_coor = np.array([(np.random.rand()*(a4 - a3) + a3) for i in range(amount)])
    res=np.array([x_coor,y_coor,(x_coor**2)+(y_coor**2),np.ones(amount)]).transpose()
    res=np.concatenate((x0,res),axis=0)
    return res


def scalar_prod(a,b):
    res=0
    for i in range(len(a)):
        res+=a[i]*b[i]
    return res


points=generate(-10,10,-10,10,1000)

label=np.zeros(len(points))
label[0]=0
for i in range(len(points)-1):
    label[i+1]=check_circle(points[i+1],center,r,epsilon)
label.mean()

alpha=np.array([0.0,0.0,0.0,0.0])

a=0
#algorithm
while(a==0):
    for i in range(len(points)):
        if alpha.dot(points[i])>=0 and label[i]==0:
            #print(i)
            alpha=alpha-points[i]
            break
        if alpha.dot(points[i])<=0 and label[i]==1:
            #print(i)
            alpha=alpha+points[i]
            break
        if i==len(points)-1:
            a=1
            break
        #alpha=alpha/alpha[2]

print(alpha)

center_y=(-1/2)*(alpha[1]/alpha[2])
print(center_y)

center_x=(-1/2)*(alpha[0]/alpha[2])
print(center_x)

rad= np.sqrt(center_x**2 + center_y**2 - alpha[3]/alpha[2])
print(rad)

check_circle([2.0,0.0],[1.0,0.0],1.0,10**(-3))
