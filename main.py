from __future__ import print_function
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Branch(object):
    def __init__(self, b):
        self.branched_from = [b]

    def add_branch(self, b):
        self.branched_from.append(b)

    def get_branched_from(self):
        return self.branched_from.pop(-1)

class Ring(object):
    def __init__(self):
        self.rings = []
        self.ring_starts = []

    def add(self, r, s):
        self.rings.append(r)
        self.ring_starts.append(s)

    def is_in(self, r):
        return r in self.rings

    def pop(self, r):
        i = self.rings.index(r)
        self.rings.pop(i)
        return self.ring_starts.pop(i)

def parse_smiles(smiles_string):
    """ returns a networkx graph based on the SMILES string description"""

    """
    TODO, not quite right for alpha-pinene. And doesn't support whatever is
    happening with lower case characters. I think it's aromatic compounds.
    """

    smiles_list = list(smiles_string.upper())
    chemical_symbols = ['H', 'B', 'C', 'N', 'O', 'P', 'S', 'F', 'Cl', 'Br', 'I']
    single_bond = '-'
    double_bond = '='
    triple_bond = '#'
    left_paren = '('
    right_paren = ')'
    ignore_characters = ['\\', '/', '@'] # used for stereochemistry

    nodes = []
    G = nx.MultiGraph()
    command = None
    prev = None
    branch = None
    ring = Ring()
    for i, char in enumerate(smiles_list):
        if char == '[':
            char = '('
        elif char == ']':
            char = ')'

        if char in chemical_symbols:
            name = char + str(len(G))
            G.add_node(name)
            if command == single_bond:
                G.add_edge(name,prev)
            if command == double_bond:
                G.add_edge(name, prev, weight=2)
            prev = name
            command = single_bond
        elif char == double_bond:
            command = double_bond
        elif char == left_paren:
            if branch is None:
                branch = Branch(prev)
            else:
                branch.add_branch(prev)
        elif char == right_paren:
            assert(branch is not None and "must have been branching, otherwise this doesn't make any sense")
            prev = branch.get_branched_from()
        elif char in map(str, range(1,10)):
            if ring.is_in(char):
                old = ring.pop(char)
                G.add_edge(old, prev)
            else:
                ring.add(char, prev)
        elif char in ignore_characters:
            pass
        else:
            print("Unrecognized char: " + char)
            print(i)
    return G

# need to add in \ to escape \
ethanol = 'CC(=C)=O'
a_pinene = 'C\\1=C(\[C@@H]2C[C@H](C/1)C2(C)C)C'
benzene = 'c1ccccc1'

g = parse_smiles(a_pinene)

#nx.draw(g)
#plt.savefig('a')


