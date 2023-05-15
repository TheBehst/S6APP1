#Eteint
VBEoff = 0.61
IDoff = 96e-6
Vpp = 10
Vmm = -10
R8 = 10e3
VB = -10 + VBEoff
B2 = 70
B3 = 200



Ib = 100e-6/((70*200)+270)
R8 = 10000
R7 = 317832.33977 #1939000000000/6100673
Rth = R8*R7/(R7+R8)
Vth = (Vpp-Vmm)*R8/(R7+R8) + Vmm

print("IB = " + str(Ib))
print("R7 = " + str(R7))
print("Rth = " + str(Rth))
print("Vth = " + str(Vth))
