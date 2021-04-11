import os
from random import choice, random
import json

data = json.load(open("Databank.json"))
num = data["num"]
nuc = data["nuc"]
met = data["met"]
ile = data["ile"]
leu = data["leu"]
phe = data["phe"]
val = data["val"]
thr = data["thr"]
pro = data["pro"]
ser = data["ser"]
ala = data["ala"]
lys = data["lys"]
asn = data["asn"]
gln = data["gln"]
his = data["his"]
stop = data["stop"]
tyr = data["tyr"]
glu = data["glu"]
asp = data["asp"]
arg = data["arg"]
trp = data["trp"]
cys = data["cys"]
gly = data["gly"]


def translate(aliases=["t"]):
    print("Enter Your RNA Sequence")
    RNA = input()
    if "T" in RNA:
        print ("Thymine cannot be present in the RNA sequence, make sure to recheck the sequence provided")
    elif choice(num) in RNA:
        print ("Integers should not be in the sequence. \n Make sure to remove the 5' and 3' if they are present")
    else:
        print(RNA)
        if choice(met) in RNA:
            print("met")
        else:
            pass
    return translate()

translate()
    


