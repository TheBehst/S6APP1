import numpy as np



pi = np.pi
r = 1070*10**(-4)
surfacePhotoDiode = pi*r**2
densiteSurfaciqueLum = 6.1
Plumineuse = densiteSurfaciqueLum*surfacePhotoDiode
responsivity = 0.55/1000 # amp per watt
photocurrent = responsivity*Plumineuse
jCap = 8*10**-12
darkCurrent = 5*10**-9
resistance = 1*10**9
print("Hello World")

print("Surface photosensible de la photodiode :" + str(surfacePhotoDiode))
print("photocurrent = "+ str(photocurrent))
print("Puissance lumineuse = "+ str(Plumineuse))

