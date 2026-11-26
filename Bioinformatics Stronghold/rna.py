dna=input()
rna=['U' if i=='T' else i for i in dna]
print("".join(rna))