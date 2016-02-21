# Chemical structure categorization

# Prototype Subproject
- Goal: determine how "stiff" a structure is
    - Hypothesis: the "stiffness" of a structure is related to the number of and nature of its conformers
    - Hypothesis: the "stiffness" of a structure is related to its reactivity
- I believe that I can create an efficient method of finding how "stiff" a structure is. 
- Stiffness Algorithm:
    - On input of a structure, the following:
    1. Compute the force-direct-layout of the structure 50 times. 
        - Call each force-directhed layout `S_i`
        - Essentially, `S_i`, is a dictionary with an `(x,y)` position for each node.
    2. Find the distribution of the layouts
        - Determine a dist'n D 
    3. Determine the entropy of the distribution. 
        - i.e. if the distribution is very uniform (the nodes go to random places) then entropy is high
        - if the structure is rigid, then the distribution should be spikier (less uniform), then lower entropy
    4. Return the entropy of the dist'n. 




