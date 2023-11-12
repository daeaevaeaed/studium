precision = 4

# Variablen
h = 25 * 10**-2
b = 28 * 10**-2
a = 44 * 10**-2
eta = 4.1065 * 10**26
mu_A = 6.29 * 10**-8
mu_K = 2.52 * 10**-8
z = 2
I_1 = 10.3
U_q = 148
e = 160.2176621 * 10**-21

# Berechnungen
J_1 = I_1 / (b * h)
I_2 = (U_q * eta * z * e * b * h * (mu_A + mu_K) / a)
print(f"J_1 = {J_1:#.{precision}g} * A/m^2")
print(f"I_2 = {I_2:#.{precision}g} * A")