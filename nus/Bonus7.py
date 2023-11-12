R = 43
Uq = 53.5
Iq = 3.97
Ub = (Uq + (2 * R * Iq))/4
if Ub > 100:
    Ub = round(Ub, -1)
else:
    Ub = round(Ub, 0)
print("Ub ist:",Ub, "* V")