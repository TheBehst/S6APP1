import numpy as np
import time

Vmm = -10
Vpp = 10

R1 = 50000
R2 = 80000
R3 = 10000000
R4 = 120000
R5 = 1
R6 = 50
R7 = 220000
R8 = 15000
R10 = 0.01
R11 = 200

temps_ini = time.perf_counter()
#===============================================================
# Photodiode
#===============================================================

r = 1070*10**(-4)
surfacePhotoDiode = np.pi*r**2
densiteSurfaciqueLum = 6.1

Plumineuse = densiteSurfaciqueLum*surfacePhotoDiode

responsivity = 0.55/1000 # amp per watt
photocurrent = responsivity*Plumineuse

jCap = 8*10**-12
darkCurrent = 5*10**-9
resistance = 1*10**9

print("\nPhotodiode:")
print("\tSurface photosensible de la photodiode :" + str(surfacePhotoDiode) + " cm\u00B2")
print("\tPhotocurrent = "+ str(photocurrent) + " A")
print("\tPuissance lumineuse = "+ str(Plumineuse) + " mW")

#===============================================================
# Etage 1
#===============================================================
Vbe1 = 0.7
Vt1 = 0.0259
Va1 = 100
B1 = 200

Ie1 = (-Vbe1-Vmm)/R3
Ib1 = Ie1/(B1+1)
Ic1 = Ie1-Ib1

Vce1 = Vpp-Vmm-R1*Ic1-R3*Ie1
Vo1 = Vpp - R1*Ic1

Rpi1 = Vt1/Ib1
R01 = Va1/Ic1
Gm1 = B1/Rpi1

print("\n\nEtage 1:")
print("\tCourant Ie a l'equilibre: "+str(Ie1)+" A")
print("\tCourant Ib a l'equilibre: "+str(Ib1)+" A")
print("\tCourant Ic a l'equilibre: "+str(Ic1)+" A")

print("\n\tVoltage Vce a l'equilibre: "+str(Vce1)+" V")
print("\tVoltage Vo1 a l'equilibre: "+str(Vo1)+" V")

print("\n\tResistance Rpi a l'equilibre: " + str(Rpi1) + " \u03A9")
print("\tResistance R0 a l'equilibre: " + str(R01) + " \u03A9")
print("\tGain Gm: " + str(Gm1) + " V/A")

#===============================================================
# Etage 2
#===============================================================
k2 = 0.00303
Vt2 = 0.7
Va2 = 130

Vg2 = (Vpp-Vmm)*R4/(R4+R2) + Vmm

coeff2 = [ k2/2 , -1/R5 - k2*Vt2 , (Vg2-Vpp)/R5 + (k2*Vt2**2)/2]

Vgs2 = -1*np.roots(coeff2)

Vov2 = Vgs2[1]-Vt2

Id2 = k2/2 * (Vgs2[1]-Vt2)**2
Vo2 = Id2*R6+Vmm
Vds2 = Vpp - Id2*(R5+R6) - Vmm
Vin2 = Vg2


ro2 = Va2/Id2

gm2 = 2*Id2/Vov2
Av2 = -(gm2*R6)/(1+(gm2*R5))
print("\n\nEtage 2:")
print("\tVoltage Vg: "+ str(Vg2) + " V")
print("\tVoltage Vgs: " + str(Vgs2[1]) + " V")
print("\t\t Calculee avec coefficient: " + str(coeff2))
print("\tCourant Id: " + str(Id2) + " A")
print("\tVoltage Vds: " + str(Vds2) + " V")
print("\tVoltage Vov: " + str(Vov2) + " V")
print("\tVoltage Vo2: " + str(Vo2) + " V")
print("\tGain Voltage : " + str(Av2) + " V")

print("\n\tResistance Ro: " + str(ro2) + " \u03A9")
print("\tGain Gm: " + str(gm2) + " A/V")

#===============================================================
# Etage 3
#===============================================================

Bq3 = 200
Bq2 = 70

Vbeq3 = 0.64
Vbeq2 = 0.59

Vdel = 2.6

Rth3 = (R8*R7)/(R8+R7)
Vth3 = (Vpp-Vmm)*R8/(R7+R8) + Vmm

Ibq3 = (Vth3-Vbeq3-Vbeq2-Vmm)/Rth3

Ic3 = (Bq3 + Bq2*Bq3 + Bq2)*Ibq3
Icq3 = (Bq3)*Ibq3
Icq2 = Ic3-Icq3

Vbq3 = Vth3 - Ibq3*Rth3

Veq3 = Vbq3-Vbeq3

Vcq3 = Vpp - Vdel

Vceq3 = Vcq3 - Veq3

Vbq2 = Veq3
Veq2 = Vmm #on neglige R10
Vcq2 = Vcq3
Vceq2 = Vcq2 - Veq2

print("\n\nEtage 3:")
print("\tResistance thevenin: "+ str(Rth3) + " \u03A9")
print("\tVoltage thevenin: "+ str(Vth3) + " V")
print("\n\tCourant Ib du macrotransistor: "+ str(Ibq3) + " A")
print("\tCourant Ic du macrotransistor: "+ str(Ic3) + " A")
print("\tCourant Ic3 du macrotransistor: "+ str(Icq3) + " A")
print("\tCourant Ic2 du macrotransistor: "+ str(Icq2) + " A")

print("\n\tVoltage Vb de Q3: "+ str(Vbq3) + " V")
print("\tVoltage Ve de Q3: "+ str(Veq3) + " V")
print("\tVoltage Vc de Q3: "+ str(Vcq3) + " V")
print("\tVoltage Vce de Q3: "+ str(Vceq3) + " V")

print("\n\tVoltage Vb de Q2: "+ str(Vbq2) + " V")
print("\tVoltage Ve de Q2: "+ str(Veq2) + " V")
print("\tVoltage Vc de Q2: "+ str(Vcq2) + " V")
print("\tVoltage Vce de Q2: "+ str(Vceq2) + " V")

#===============================================================
# DEL
#===============================================================

Dp = 8.5 # cm^2
Dn = 1.84e2 # cm^2

Lp = 1.61e-5
Ln = 5.09e-5

Nd = 1e17
Na = Nd

A = np.pi*((0.13/2)**2)

ni = 2.18e6
q = 1.6e-19

Vt = 25.9e-3
e0 = 8.854e-14
es = 11.7*e0
Is = A*q*(ni**2)*((Dp/(Lp*Nd))+(Dn/(Ln*Na)))


v0 = Vt*np.log((Na*Nd)/ni**2)
cj0 = A* np.sqrt((es*q/2)*((Na*Nd)/(Na+Nd))*(1/v0))
print("\n\nDel:")
print("\tIs: "+ str(Is) + " A")
print("\tJunction built-in voltage : "+str(v0) + " V")
print("\tcapacite de jonction Cj0 : " + str(cj0) + " F")

#===============================================================
# Misc
#===============================================================

print("\n\n\nTemps de calcul: " + str(1000*(time.perf_counter()-temps_ini)) + " ms")


