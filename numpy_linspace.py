'''import numpy as np

print("B \n",np.linspace(2.0,3.0,5,retstep=False),"\n")

x=np.linspace(0,2,10)

print("A\n",np.sin(x))
      
'''
'''
import numpy as np

b=np.eye(2, dtype=float)

print("Matrix b: \n",b)

a=np.eye(4,5,k= 1)
print("\n Matrix a: \n",a)
    
'''
import numpy as np
from matplotlib import pyplot as plt

x=np.linspace(-4,4,9)

y=np.linspace(-5,5,11)


x_1,y_1=np.meshgrid(x,y)

print("x_1= \n")

print(x_1)

print("y_1 = \n")

print(y_1)

ellipse = x_1 * 2 + 4 * y_1**2


plt.contourf(x_1,y_1,ellipse,cmap='jet')
plt.colorbar()
plt.show()

'''
random_data = np.random.random((11, 9))

x=np.linspace(-4,4,9)

y=np.linspace(-5,5,11)


x_1,y_1=np.meshgrid(x,y)

plt.contourf(x_1, y_1, random_data, cmap = 'jet') 
  
plt.colorbar()
plt.show()
'''
























