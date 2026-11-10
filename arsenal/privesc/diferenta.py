import json, os
from enumm import citeste_linii

def cai(fisier):
    return set(citeste_linii(fisier))

baza = cai("start/baza_suid.txt")
acum = cai("start/suid.txt")
print("baza:", len(baza), " acum:", len(acum))