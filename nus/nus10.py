import numpy as np
a = 0.0287
A= a**2
lg= 0.001
lr= 0.271
mu1= 1564
N= 840
I= 0.999
RmL=lg/(A*1.25663706212e-6)
RmM=RmL
RmR=lr/(A*1.25663706212e-6*mu1)
D=N*I                                            # Windungszahl, Strom, länge R, länge G 2
phir=(2*D*A*1.25663706212e-6*mu1)/(2*lr+(mu1*lg)) # (2*Fluss*Fläche*mu0*mu1)/(2*längeR + (mu1*länge G))
phim=phir/2
phil=phim
AL=(2*A*1.25663706212e-6*mu1)/(2*lr+(mu1*lg))
print(RmL, "rml")
print(RmM, "RmM")
print(RmR, "RmR")
print(D, "D")
print(phir, "PhiR")
print(phim, "PhiM")
print(phil, "PhiL")
print(AL, "AL")