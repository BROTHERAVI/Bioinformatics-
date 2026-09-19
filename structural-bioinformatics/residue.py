with open('1ltx.pdb', 'r') as file:
    file_path = file.readlines()

residues = []
amino_acids = {}
for line in file_path:
    if line.startswith('ATOM') and line[21] == 'B':
        residue = int(line[22:26].strip())
        amino_acid = line[17:20].strip()
        if residue not in residues:
            residues.append(residue)
            amino_acids[residue] = amino_acid

midpoint = len(residues) // 2
center_residue = residues[midpoint]
center_amino_acid = amino_acids[center_residue]

print("The center most residue in chain B is:", center_residue)
print("The corresponding amino acid is:", center_amino_acid)
