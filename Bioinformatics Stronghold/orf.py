import sys
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
codon_table = {
    "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
    "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
    "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
    "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
    "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
    "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
    "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "TAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "TAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
    "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "TGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G",
}
seqs=read_fasta(sys.stdin.read())


temp=next(iter(seqs.values()))
length=len(temp)

base_paring=temp.maketrans("ACGT", "TGCA")
comp=temp.translate(base_paring)
rcomp=comp[::-1]
ans_temp=[[]]
ans_rcomp=[[]]
def orf(temp,ans_temp):
    for i in range(3):
        current_working=[]
        overlap=[0]
        for j in range(i,length-2,3):
            codon=temp[j:j+3]
            if not current_working:
                if codon_table[codon]=="M":
                    current_working.append("M")
            elif codon_table[codon]=="Stop":
                for k in overlap:
                    ans_temp.append(current_working[k:])
                current_working=[]
                overlap=[0]
            elif codon_table[codon]=="M":
                overlap.append(len(current_working))
                current_working.append("M")
            else:
                current_working.append(codon_table[codon])
    return ans_temp
ans_temp=orf(temp,ans_temp)
ans_rcomp=orf(rcomp,ans_rcomp)
found = set()
for protein in ans_temp+ans_rcomp:
    if protein:
        found.add("".join(protein))
print("\n".join(found))

            


