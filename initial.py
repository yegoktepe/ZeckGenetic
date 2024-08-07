# -*- coding: utf-8 -*-

# Initialisations

chromosomes = []
zeckChromosomes = []
kzeckChromosomes = []
fitness = []
zeckFitness = []
kzeckFitness = []
possibilities = []
zeckPossibilities = []
kzeckPossibilities = []
selectionCount = []
zeckSelectionCount = []
kzeckSelectionCount = []
stringChromosomes = []
zeckStringChromosomes = []
kzeckStringChromosomes = []
mutationChromosomes = []


fibos=[]
for i in range(25) :
    if i<2:
        fibos.append(i+1)
    else: 
        fibos.append(fibos[i-1]+fibos[i-2])

population=500

coefficient5=6; coefficient4=-3; coefficient3=4; coefficient2=-2; coefficient1=9; coefficient0=-7;

genCount=14; zeckGenCount=19; kzeckGenCount=19
bitCount=0; zeckBitCount=0; kzeckBitCount=0
crossoverPoint=int(genCount*0.618)
zeckCrossoverPoint=int(zeckGenCount*0.618)
