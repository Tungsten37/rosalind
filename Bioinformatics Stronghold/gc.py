import sys
def read_fasta(text):
    sequences = {}
    current_seq = []
    for line in text.splitlines():
        line = line.strip()
        if line[0]=='>':
            if current_seq:
                sequences[header] = (''.join(current_seq))
                current_seq = []
            header = line[1:] 
        else:
            current_seq.append(line)
    if current_seq:
        sequences[header] = (''.join(current_seq))
    return sequences

seqs=read_fasta(sys.stdin.read())
gcish=next(iter(seqs))
gcish_percent=0
for header, seq in seqs.items():
    gc_count = seq.count('G') + seq.count('C')
    gc_percent = (gc_count / len(seq)) * 100
    if gc_percent>gcish_percent:
        gcish=header
        gcish_percent=gc_percent
print(gcish,gc_percent,sep='\n')
