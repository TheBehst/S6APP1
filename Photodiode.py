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
tension = (Plumineuse/photocurrent)/1000
Gain = photocurrent/(Plumineuse/1000)
print("Hello World")

print("Surface photosensible de la photodiode :" + str(surfacePhotoDiode))
print("photocurrent = "+ str(photocurrent) + " A")
print("Puissance lumineuse = "+ str(Plumineuse) + " mW")
print("tension : " + str(tension) + " V")
print("Gain : " + str(Gain))

print("------------impedance entree etage 1---------------")
ve1 = 14621
iR1 = 1
z1 = ve1/iR1
print("impedance entree etage 1 : " + str(z1))

vi2 = 4.97593e-015
iC1 = -9.95186e-020
z2 = vi2/iC1

