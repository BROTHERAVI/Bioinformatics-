aa_hydro = ['ALA','ILE','LEU','MET','PHE','PRO','VAL','TRP','TYR']
count = 0
pdbfile = open(input("please type your PDB filename:")).readlines()

for line in pdbfile:
    if line.startswith('ATOM'):
        count += 1

print(count)
