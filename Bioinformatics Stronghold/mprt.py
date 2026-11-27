from urllib.request import urlopen
import sys
import re
def fetch_uniprot(uid):
    acc = uid.split("_")[0]
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urlopen(url) as res:
        return res.read().decode()
def read_fasta(text):
    sequences = {}
    current_seq = []
    for line in text.splitlines():
        line = line.strip()
        if not line:continue
        if line.startswith(">"):
            if current_seq:
                sequences[header] = (''.join(current_seq))
                current_seq = []
            header = line[1:] 
        else:
            current_seq.append(line)
    if current_seq:
        sequences[header] = ''.join(current_seq)
    return sequences

with open("input.txt", "r") as f:
    for line in f:
        uid=line.strip()
        prt=next(iter(read_fasta(fetch_uniprot(uid)).values()))
        motives = re.finditer("(?=N[^P][ST][^P])",prt)
        positions=[motif.start()+1 for motif in motives]
        if positions:
            print(uid)
            print(*positions)