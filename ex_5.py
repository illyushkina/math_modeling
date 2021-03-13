
import numpy as np

def f(key=0,h=0,l=0,r=0,a=0,b=0):
  if key==0:
    S=1/2*h*l
  if key==1:
    S=np.pi*r**2
  if key==2:
    S=a*b/2
  print(S)



f(key=0,h=8,l=5)



