import math
result = ""
dez = 2621
while (dez > 0):
    result = str(dez % 16) + result
    dez = math.floor(dez / 16)

print(result)