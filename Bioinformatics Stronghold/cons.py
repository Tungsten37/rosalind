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

seqs=read_fasta(sys.stdin.read())
length=len(next(iter(seqs.values())))
profile={"A":[0]*length,"C":[0]*length,"G":[0]*length,"T":[0]*length,} #A, C, G, Tの順
consensus=["A"]*length
for k in range(length):
    for j in seqs.values():
        profile[j[k]][k]+=1
    mostused=0
    for i,j in profile.items():
        if j[k]>=mostused:
            mostused=j[k]
            consensus[k]=i
print("".join(consensus))
for i,j in profile.items():
    print(i+":",*j)
