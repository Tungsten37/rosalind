str=input()
base_paring=str.maketrans("ACGT", "TGCA")
comp=str.translate(base_paring)
print(comp[::-1])
