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
print("linii SUID:", len(cai))