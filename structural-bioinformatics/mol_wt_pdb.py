pdbfile = open(input("please type your PDB filename:")).readlines()
molwt = 0
for i in range(0, len(pdbfile)):
    line = pdbfile[i].rstrip()
    if line[13:14] == 'N':
        molwt = molwt + 14
    elif line[13:14] == 'O':
        molwt = molwt + 16
    elif line[13:14] == 'C':
        molwt = molwt + 12
    elif line[13:14] == 'S':
        molwt = molwt + 32
    elif line[13:14] == 'H':
        molwt = molwt + 1

print("The molecular weight of this protein is:", molwt)
