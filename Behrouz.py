import numpy as np
#Eteint
VBEoff = 0.61
Vpp = 3.3
Vmm = -3.3
VB = Vmm + VBEoff
R6 = 120

#on pose R8 est egale a Zbase (etat ON)
gm = (2.5 - 90e-6) / (1.82 - 0.61)
beta2 = 70
beta3 = 200
beta_global = beta2 + beta3 + beta2*beta3
alpha = beta_global / (beta_global + 1)
re = alpha/gm
R10 = 0.01
Zbase = (beta_global + 1) * (re + R10)
R8 = Zbase

#on trouve R7
Ib = 90e-6/beta_global
R7 = (R8 * (Vpp - VB)) / (VB - Vmm + Ib * R8)

# code de sauce a behrouz
Rth = R8*R7/(R7+R8)
Vth = (Vpp-Vmm)*R8/(R7+R8) + Vmm

#Zin etage 3
Zin = 1 / ((1/Zbase) + (1/R7) + (1/R8))
fcC2 = 5e3
ZeqC2 = Zin + R6
C2 = 1/(2*np.pi*fcC2*ZeqC2)

print("Zbase = " + str(Zbase))
print("Gm = " + str(gm))
print("IB = " + str(Ib))
print("R7 = " + str(R7))
print("R8 = " + str(R8))
print("Zin = " + str(Zin))
print("C2 = " + str(C2))
print("Rth = " + str(Rth))
print("Vth = " + str(Vth))
