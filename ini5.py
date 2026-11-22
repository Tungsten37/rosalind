with open("rosalind_ini5.txt") as f, open("ini5_ans.txt", "w") as out:
    for i, line in enumerate(f, start=1):
        if i % 2 == 0:
            out.write(line)
