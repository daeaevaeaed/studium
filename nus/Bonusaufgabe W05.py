# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:05:36 2023

@author: rishy
"""

import numpy as np

#Bekannte Werte
U_q=float(input("U_q="))
R_1=float(input("R_1="))
R_2=float(input("R_2="))
R_3=float(input("R_3="))
R_4=float(input("R_4="))

#Berechnungen
I_1=U_q/R_1
I_2=U_q/(R_2+R_4)
I_3=U_q/R_3
I_30=U_q/R_2

I=I_1+I_2+I_3

U_2=R_4*I_2

R_10=U_q/I

R_30=U_2/I_30

X_var = ["U_2","R_10","R_30"]
X_results = [U_2,R_10,R_30]
Einheit=["V","ohm","ohm"]
#Resultate
print(" ")
print("Resultate:")
n=0
while(n<len(X_var)):
    print (X_var[n],"=",float('%.3g' % X_results[n]),"*",Einheit[n])
    n=n+1