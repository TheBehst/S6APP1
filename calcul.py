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

ro2 = Va2/Id2

gm2 = 2*Id2/Vov2

print("\n\nEtage 2:")
print("\tVoltage Vg: "+ str(Vg2) + " V")
print("\tVoltage Vgs: " + str(Vgs2[1]) + " V")
print("\t\t Calculee avec coefficient: " + str(coeff2))
print("\tCourant Id: " + str(Id2) + " A")
print("\tVoltage Vds: " + str(Vds2) + " V")
print("\tVoltage Vov: " + str(Vov2) + " V")
print("\tVoltage Vo2: " + str(Vo2) + " V")

print("\n\tResistance Ro: " + str(ro2) + " \u03A9")
print("\tGain Gm: " + str(gm2) + " A/V")

#===============================================================
# Etage 3
#===============================================================

Bq3 = 200
Bq2 = 70

Vbeq3 = 0.64
Vbeq2 = 0.59

Rth3 = (R8*R7)/(R8+R7)
Vth3 = (Vpp-Vmm)*R8/(R7+R8) + Vmm

Ibq3 = (Vth3-Vbeq3-Vbeq2-Vmm)/Rth3

Ic3 = (Bq3 + Bq2*Bq3 + Bq2)*Ibq3
Icq3 = (Bq3)*Ibq3
Icq2 = Ic3-Icq3

print("\n\nEtage 3:")
print("\tResistance thevenin: "+ str(Rth3) + " \u03A9")
print("\tVoltage thevenin: "+ str(Vth3) + " V")
print("\n\tCourant Ib du macrotransistor: "+ str(Ibq3) + " A")
print("\tCourant Ic du macrotransistor: "+ str(Ic3) + " A")
print("\tCourant Ic3 du macrotransistor: "+ str(Icq3) + " A")
print("\tCourant Ic2 du macrotransistor: "+ str(Icq2) + " A")


#===============================================================
# Misc
#===============================================================

print("\n\n\nTemps de calcul: " + str(1000*(time.perf_counter()-temps_ini)) + " ms")



