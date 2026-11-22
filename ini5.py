with open("rosalind_ini5.txt") as input, open("ini5_ans.txt", "w") as output:
    for line_number, line_text in enumerate(input, start=1):
        if line_number % 2 == 0:
            output.write(line_text)
