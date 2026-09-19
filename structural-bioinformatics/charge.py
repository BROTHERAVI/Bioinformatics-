charge_dict = {'LYS': 1, 'ARG': 1, 'ASP': -1, 'GLU': -1}
total_charge = 0

with open("1ltx.pdb", 'r') as pdb_file:
    for line in pdb_file:
        if line.startswith("ATOM"):
            residue_name = line[17:20].strip()
            if residue_name in charge_dict:
                total_charge += charge_dict[residue_name]

print(f"Total charge of the protein: {total_charge}")
