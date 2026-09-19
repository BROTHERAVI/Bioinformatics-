def count_nitrogen_atoms(pdb_file):
    count = 0
    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith('ATOM'):
                atom_name = line[12:16].strip()
                if atom_name == 'N':
                    count += 1
    return count

nitrogen_count = count_nitrogen_atoms('1ltx.pdb')
print(f'The number of nitrogen (N) atoms in the PDB file is: {nitrogen_count}')
