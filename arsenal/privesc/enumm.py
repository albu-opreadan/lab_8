import argparse, json, os

def citeste_linii(cale):
    with open(cale, encoding="utf-8") as f:
        linii = []
        for linie in f:
            linie = linie.strip()
            if not linie or linie.startswith("#"):
                continue
            linii.append(linie)
        return linii

cai = citeste_linii("start/suid.txt")
#print("linii SUID:", len(cai))


def nume(cale):
    return cale.rsplit("/", 1)[-1]

nume_unice = {nume(c) for c in cai} 
print("SUID distincte:", len(nume_unice))