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
#print("SUID distincte:", len(nume_unice))


GTFO = {"find", "vim.basic", "vim", "nmap", "cp", "bash",
        "less", "awk", "python3", "perl"}

def suid_constatari(cale):
    cai = citeste_linii(cale)
    constatari = []
    for c in sorted(set(cai)):
        constatari.append({
            "cale": c,
            "nume": nume(c),
            "risc": "mare" if nume(c) in GTFO else "normal"
        })
    return constatari

suid = suid_constatari("start/suid.txt")
mari = [c for c in suid if c["risc"] == "mare"]
print(len(suid), "SUID,", len(mari), "cu risc mare")
print(sorted(c["nume"] for c in mari))


def sudo_constatari(cale):
    out = []
    for ln in citeste_linii(cale):
        user, drept = ln.split(" : ", 1)
        out.append({
            "user": user.strip(),
            "drept": drept.strip(),
            "risc": "mare" if "NOPASSWD" in drept else "normal"
        })
    return out