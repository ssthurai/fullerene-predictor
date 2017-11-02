''' @package fullerene.py
A class that stores information about a Fullerene.
'''
import copy
from process_input import process_atoms_array, process_connectivity, \
    process_5_rings, process_6_rings

def compute_ring_connectivity(rings, rings_lookup):
    '''
    compute_ring_connectivity determine which rings are connected to each other.

    @param rings list of rings in the
    '''
    ring_connectivity = []
    for i in range(0, len(rings)):
        temp_list = []
        for j in range(0, len(rings[i])):
            neighbor_ring = rings_lookup[rings[i][j]]
            temp_list.extend(neighbor_ring)
        temp_set = set(temp_list)
        temp_set.remove(i)
        ring_connectivity.append(list(temp_set))

    return ring_connectivity

class Fullerene:
    '''!
    Stores a description of a given Fullerene system.
    '''

    def __init__(self, file_name):
        '''!
        __init__ initialize a Fullerene object from file.

        self: Fullerne to initialize.
        file_name: Filename to initialize from.
        '''
        self.atoms_array = process_atoms_array(file_name)
        self.connectivity = process_connectivity(file_name,
                                                 len(self.atoms_array))
        fiverings, fiverings_center = process_5_rings(file_name)
        sixrings, sixrings_center = process_6_rings(file_name)

        self.ring_list = copy.copy(fiverings)
        self.ring_list.extend(sixrings)

        self.ring_center = copy.copy(fiverings_center)
        self.ring_center.extend(sixrings_center)

        self.ring_lookup = []
        for i in range(0, len(self.atoms_array)):
            self.ring_lookup.append([])
        for i in range(0, len(self.ring_list)):
            for atom in self.ring_list[i]:
                self.ring_lookup[atom].append(i)


        self.rings_connectivity = compute_ring_connectivity(self.ring_list,
                                                       self.ring_lookup)
