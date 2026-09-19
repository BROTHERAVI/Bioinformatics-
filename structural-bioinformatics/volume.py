radii = {'H': 120, 'O': 152, 'C': 170, 'N': 155, 'S': 180}

def volume(radius):
    return (4/3) * 3.14 * (radius**3)

total_volume = 0
with open('1ltx.pdb', 'r') as pdbfile:
    for line in pdbfile:
        if line.startswith('ATOM'):
            if line[13:14] == 'C':
                total_volume += volume(radii['C'])
            elif line[13:14] == 'N':
                total_volume += volume(radii['N'])

print(f'Total volume of atom: {total_volume:.3f}')
