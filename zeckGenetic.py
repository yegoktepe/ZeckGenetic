# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from tkinter import *
import random
import math

execfile('initial.py')


def fitness_function(x):
    ftnss=(coefficient5*x**5)+(coefficient4*x**4)+(coefficient3*x**3)+(coefficient2*x*x)+(coefficient1*x)+coefficient0
    # print(x , " ",ftnss)
    return ftnss


def findChromosomeWithMaxSelectionCount():
    mx=1
    for j in range(population):
        if selectionCount[j]>mx:
            mx=j
            #print("j=",j, "selectionCount[j]", selectionCount[j],"max=",mx)
    return mx

def findZeckChromosomeWithMaxSelectionCount():
    mx=1
    for j in range(population):
        if zeckSelectionCount[j]>mx:
            mx=j
            #print("j=",j, "selectionCount[j]", selectionCount[j],"max=",mx)
    return mx

def crossover(chromosome1,chromosome2,point):
    newChr1=chromosome1[0:point]+chromosome2[point:len(chromosome1)]
    newChr2=chromosome2[0:point]+chromosome1[point:len(chromosome1)]
    # print("co:",chromosome1, chromosome2, point)
    # print("co:",newChr1, newChr2)
    return newChr1, newChr2
    
    # p1,p2 = list(parent1),list(parent2) #convert str to list
    # print("\n",p1, p2)
    # for i in range(point,len(p1)):
    #     print("i:",i, "point:",point,"len p1:",len(p1))
    #     p1[i],p2[i] = p2[i],p1[i]       #swap the genetic information
    # p1,p2 = ''.join(p1),''.join(p2)     #Convert list to str
    # #print(p1,"ee",p2)
    # return p1,p2

def mutation(chromosome, index):
    #print("chromosome ", chromosome, " index:", index, "gen:",chromosome[index:index+1])
    if chromosome[index:index+1]=="0" : 
        chromosome = chromosome[0:index]+"1"+chromosome[index+1:genCount]
    else: 
        chromosome = chromosome[0:index]+"0"+chromosome[index+1:genCount]
    #print("chromosome", chromosome)
    return chromosome


def zeckMutation(chromosome, index):
    #print("chromosome ", chromosome, " index:", index, "gen:",chromosome[index:index+1])
    if chromosome[index:index+1]=="0" : 
        chromosome = chromosome[0:index]+"1"+chromosome[index+1:zeckGenCount]
    else: 
        chromosome = chromosome[0:index]+"0"+chromosome[index+1:zeckGenCount]
    #print("chromosome", chromosome)
    return chromosome

def convertToDecimal(chromosome):
    value=0
    #print(chromosome)
    for j in range(genCount):
        #print("j:",j)
        if chromosome[j] == "1":
            value+=pow(2,(genCount-1-j))
    return value

def zeckConvertToDecimal(chromosome):
    value=0
    #print("chromosome",chromosome)
    for j in range(zeckGenCount):
        # print("j:", j, "length:", len(chromosome), chromosome)
        if chromosome[j] == "1":
            #print(fibos[zeckGenCount-1-j])
            value+=fibos[zeckGenCount-1-j]
    return value

def convertToString(chromosome):
    chromosome=str(bin(int(chromosome)))
    chromosome=chromosome[2:len(chromosome)]
    for i in range(genCount-len(chromosome)):
        chromosome="0"+chromosome
    return chromosome

def zeckConvertToString(chromosome):
    newChr=""
    for i in range(zeckGenCount):    
        if chromosome>=fibos[zeckGenCount-1-i]:
            newChr=newChr+"1"
            chromosome-=fibos[zeckGenCount-1-i]
            #print("i:",i,"chromosome:", chromosome, "Y",fibos[11-i])
        else: 
            newChr=newChr +"0" 
            #print("i:",i,fibos[11-i])
    #print("chromosome:",newChr)
    return newChr   

def zirkofDonusum(chromosome):
    #print("chromosome",chromosome, zeckConvertToDecimal(str(chromosome)))
    #print("chromosome:",chromosome)
    continuee=True
    while(continuee):
        continuee=False
        for i in range(zeckGenCount-2):
            #print("i:",i)
            if chromosome[i]=="1" and chromosome[i+1]=="0" and chromosome[i+2]=="0":
                chromosome = chromosome[0:i] +"011"+chromosome[i+3:zeckGenCount+1]
                devam=True
                break;
    #print("chromosome", chromosome, zeckConvertToDecimal(str(chromosome)))
    return chromosome

for i in range(population):
    fitness.append(float(0))
    zeckFitness.append(float(0))
    kzeckFitness.append(float(0))
    possibilities.append(float(0))
    zeckPossibilities.append(float(0))
    kzeckPossibilities.append(float(0))
    selectionCount.append(float(0))
    zeckSelectionCount.append(float(0))
    kzeckSelectionCount.append(float(0))
    stringChromosomes.append(str(0))
    zeckStringChromosomes.append(str(0))
    kzeckStringChromosomes.append(str(0))
    sayi=round(random.random()*20,0)
    chromosomes.append(float(sayi))
    zeckChromosomes.append(float(sayi))
    kzeckChromosomes.append(float(sayi))
for i in range(10000):
    mutationChromosomes.append(0)
    
coefficient5=float(input("Coefficient of 5th. degree element?:"))
coefficient4=float(input("Coefficient of 4th. degree element?:"))
coefficient3=float(input("Coefficient of 3th. degree element?:"))
coefficient2=float(input("Coefficient of 2th. degree element?:"))
coefficient1=float(input("Coefficient of 1th. degree element?:"))
coefficient0=float(input("Constant element?:"))

globalMaxFitnessValue=0
zeckGlobalMaxFitnessValue=0
zeckGlobalMaxFitnessValueZD=0

globalMaxChromosomeValue=0
zeckGlobalMaxChromosomeValue=0
zeckGlobalMaxChromosomeValueZD=0

maxKromozomDegeriArtisi=0
maxFitnessDegeriArtisi=0
ToplamFitnessDegeriArtisi=0
maxToplamFitnessDegeri=0
fiboMaxToplamFitnessDegeri=0
fiboMaxToplamFitnessDegeriZD=0

epoch=1

for i in range(population):
        zeckStringChromosomes[i]=zeckConvertToString(zeckChromosomes[i])
        kzeckStringChromosomes[i]=zeckConvertToString((kzeckChromosomes[i]))
        kzeckStringChromosomes[i]=zirkofDonusum(kzeckStringChromosomes[i])

mutationRate=((math.sqrt(5)-1)/2)
epochCount=50
while epoch<epochCount:
    
    # print("chromosomes    :",chromosomes)
    # print("chromosomes   F:",zeckChromosomes)
    
    for i in range(population):
        stringChromosomes[i]=convertToString(chromosomes[i])
    #print("Str chromosomes:",stringChromosomes)
    
    for i in range(population):
        zeckStringChromosomes[i]=zeckConvertToString(zeckChromosomes[i])
        kzeckStringChromosomes[i]=zeckConvertToString((kzeckChromosomes[i]))
        kzeckStringChromosomes[i]=zirkofDonusum(kzeckStringChromosomes[i])
    # print("Fib chromosomes 1:",zeckStringChromosomes)
    # print("Fib chromosomesZD:",kzeckStringChromosomes)
    
    totalFitness=0
    bestFitness=0
    for i in range(population):
        fitness[i]=float(fitness_function(float(chromosomes[i])))
        totalFitness+=fitness[i]
        if fitness[i]>bestFitness:
            bestFitness=fitness[i]
        if fitness[i]>globalMaxFitnessValue:
            globalMaxFitnessValue=fitness[i]
            globalMaxChromosomeValue=chromosomes[i]    
    # print("Fitnesses    :",Fitness, globalMaxFitnessValue)
    # print("totalFitness :",totalFitness, "Best Fitness:",bestFitness)
        

    zeckTotalFitness=0
    bestFitness=0
    for i in range(population):
        zeckFitness[i]=float(fitness_function(float(zeckChromosomes[i])))
        zeckTotalFitness+=zeckFitness[i]  
        if zeckFitness[i]>bestFitness:
            bestFitness=zeckFitness[i] 
        if zeckFitness[i]>zeckGlobalMaxFitnessValue:
            zeckGlobalMaxFitnessValue=zeckFitness[i]
            zeckGlobalMaxChromosomeValue=zeckChromosomes[i]
    # print("Fitnesses   F:",zeckFitness, zeckGlobalMaxFitnessValue)
    # print("totalFitnessF:",zeckTotalFitness, "Best Fitness:",bestFitness)

    kzeckTotalFitness=0
    bestFitness=0
    for i in range(population):
        kzeckFitness[i]=float(fitness_function(float(kzeckChromosomes[i])))
        kzeckTotalFitness+=kzeckFitness[i]  
        if kzeckFitness[i]>bestFitness:
            bestFitness=kzeckFitness[i] 
        if kzeckFitness[i]>zeckGlobalMaxFitnessValueZD:
            zeckGlobalMaxFitnessValueZD=kzeckFitness[i]
            zeckGlobalMaxChromosomeValueZD=kzeckChromosomes[i]
    #print("Fitnesses   F:",zeckFitness)
    #print("totalFitnessF:",zeckTotalFitness, "Best Fitness:",bestFitness)
   
    for i in range(population):
        possibilities[i]=fitness[i] / totalFitness
    #print("Possibilities    :", possibilities)
    
    for i in range(population):
        zeckPossibilities[i]=zeckFitness[i] / zeckTotalFitness
    #print("Possibilities   F:", zeckPossibilities)
    
    for i in range(population):
        kzeckPossibilities[i]=kzeckFitness[i] / kzeckTotalFitness
    #print("Possibilities   F:", kzeckPossibilities)
        
    for i in range(population):
        selectionCount[i]=round(possibilities[i]*population,0)
    #print("Selection Counts :", selectionCount)
    
    for i in range(population):
        zeckSelectionCount[i]=round(zeckPossibilities[i]*population,0)
    #print("Selection CountsF:", zeckSelectionCount)
    
    for i in range(population):
        kzeckSelectionCount[i]=round(kzeckPossibilities[i]*population,0)
    #print("Selection CountsF:", kzeckSelectionCount)
    
    for i in range(population):
        if selectionCount[i]==0:
            chromosomeWithMaxSelectionCount=int(findChromosomeWithMaxSelectionCount())
            chromosomes[i]=chromosomes[chromosomeWithMaxSelectionCount]
            selectionCount[chromosomeWithMaxSelectionCount]-=1
            selectionCount[i]+=1
            #print("Selection Counts:", selectionCount)  
    #print("chromosomes    :",chromosomes)
    
    for i in range(population):
        if zeckSelectionCount[i]==0:
            chromosomeWithMaxSelectionCount=int(findZeckChromosomeWithMaxSelectionCount())
            zeckChromosomes[i]=zeckChromosomes[chromosomeWithMaxSelectionCount]
            zeckSelectionCount[chromosomeWithMaxSelectionCount]-=1
            zeckSelectionCount[i]+=1
            #print("Selection Counts:", selectionCount)  
    #print("chromosomes   F:",zeckChromosomes)
    
    for i in range(population):
        if kzeckSelectionCount[i]==0:
            chromosomeWithMaxSelectionCount=int(findZeckChromosomeWithMaxSelectionCount())
            kzeckChromosomes[i]=kzeckChromosomes[chromosomeWithMaxSelectionCount]
            kzeckSelectionCount[chromosomeWithMaxSelectionCount]-=1
            kzeckSelectionCount[i]+=1
            #print("Selection Counts:", selectionCount)  
    #print("chromosomes   F:",kzeckChromosomes)

    
    for i in range(population):
        stringChromosomes[i]=convertToString(chromosomes[i])
    #print("String Chromosomes   :",stringChromosomes)
    
    for i in range(population):
        zeckStringChromosomes[i]=zeckConvertToString(zeckChromosomes[i])
        kzeckStringChromosomes[i]=zirkofDonusum(zeckStringChromosomes[i])
    #print("Zeck String Chromosomes:",zeckStringChromosomes)
    
    for i in range(int(population/2)):
        stringChromosomes[i*2], stringChromosomes[i*2+1] = crossover(stringChromosomes[i*2], stringChromosomes[i*2+1], crossoverPoint)

    for i in range(int(population/2)):
        #print(i*2, i*2+1,zeckChromosomes[i*2],zeckChromosomes[i*2+1],zeckStringChromosomes[i*2], zeckStringChromosomes[i*2+1])
        zeckStringChromosomes[i*2], zeckStringChromosomes[i*2+1] = crossover(zeckStringChromosomes[i*2], zeckStringChromosomes[i*2+1], zeckCrossoverPoint)
    
    for i in range(int(population/2)):
        #print(i*2, i*2+1,zeckChromosomes[i*2],zeckChromosomes[i*2+1],zeckStringChromosomes[i*2], zeckStringChromosomes[i*2+1])
        kzeckStringChromosomes[i*2], kzeckStringChromosomes[i*2+1] = crossover(kzeckStringChromosomes[i*2], kzeckStringChromosomes[i*2+1], zeckCrossoverPoint)
    
    bitCount=population*genCount  
    mutationCount=int(round(bitCount*mutationRate,0))

    for j in range(mutationCount):
        mutationGenPoint=round(random.random()*bitCount,0)
        mutationChromosomeNo, mutationIndex=divmod(mutationGenPoint, genCount)
        mutationChromosomeNo=int(mutationChromosomeNo-1)
        mutationChromosomes[j]=(chromosomes[mutationChromosomeNo])
        stringChromosomes[mutationChromosomeNo]=mutation(stringChromosomes[mutationChromosomeNo], int(mutationIndex))

    zeckBitCount=population*zeckGenCount
    zeckMutationCount=int(round(zeckBitCount*mutationRate,0))

    for j in range(zeckMutationCount):
        mutationGenPoint=round(random.random()*zeckBitCount,0)
        mutationChromosomeNo, mutationIndex=divmod(mutationGenPoint, zeckGenCount)
        mutationChromosomeNo=int(mutationChromosomeNo-1)
        mutationChromosomes[j]=(zeckChromosomes[mutationChromosomeNo])
        zeckStringChromosomes[mutationChromosomeNo]=zeckMutation(zeckStringChromosomes[mutationChromosomeNo], int(mutationIndex))

    kzeckBitCount=population*zeckGenCount
    zeckMutationCountZD=int(round(zeckBitCount*mutationRate,0))

    for j in range(zeckMutationCountZD):
        mutationGenPoint=round(random.random()*kzeckBitCount,0)
        mutationChromosomeNo, mutationIndex=divmod(mutationGenPoint, kzeckGenCount)
        mutationChromosomeNo=int(mutationChromosomeNo-1)
        mutationChromosomes[j]=(kzeckChromosomes[mutationChromosomeNo])
        kzeckStringChromosomes[mutationChromosomeNo]=zeckMutation(kzeckStringChromosomes[mutationChromosomeNo], int(mutationIndex))

    for i in range(population):
        chromosomes[i]=convertToDecimal(stringChromosomes[i])
    for i in range(population):    
        zeckChromosomes[i]=zeckConvertToDecimal(str(zeckStringChromosomes[i]))    
    for i in range(population):    
        kzeckChromosomes[i]=zeckConvertToDecimal(str(kzeckStringChromosomes[i]))    

    epoch+=1


print("\nGlobal Max Chromosome Value:", globalMaxChromosomeValue, "Zeckendorf Max Chromosome Value:", zeckGlobalMaxChromosomeValue, "k-Zeckendırf Max Chromosome Value:", zeckGlobalMaxChromosomeValueZD)
print("Increase Rate Based on Chromosomal Value")
print("Genetic - Zeckendorf      : %", (zeckGlobalMaxChromosomeValue-globalMaxChromosomeValue)*100/globalMaxChromosomeValue)
print("Genetic - k-Zeckendorf    : %", (zeckGlobalMaxChromosomeValueZD-globalMaxChromosomeValue)*100/globalMaxChromosomeValue)
print("Zeckendorf - k-Zeckendorf : %", (zeckGlobalMaxChromosomeValueZD-zeckGlobalMaxChromosomeValue)*100/zeckGlobalMaxChromosomeValue, "\n")
    
    
print("\nnGlobal Max Fitness Value:", globalMaxFitnessValue, "Zeckendorf Max Fitness Value:", zeckGlobalMaxFitnessValue, "k-Zeckendorf Max Fitness Value:", zeckGlobalMaxFitnessValueZD)
print("Increase Rate in Max Chromosome Fitness Value")
print("Genetic - Zeckendorf      : %",(zeckGlobalMaxFitnessValue-globalMaxFitnessValue)*100/globalMaxFitnessValue)
print("Genetic - k-Zeckendorf    : %",(zeckGlobalMaxFitnessValueZD-globalMaxFitnessValue)*100/globalMaxFitnessValue)
print("Zeckendorf - k-Zeckendorf : %",(zeckGlobalMaxFitnessValueZD-zeckGlobalMaxFitnessValue)*100/zeckGlobalMaxFitnessValue)

# print("Global Toplam Fitness Değeri:", totalFitness, " Fibo Toplam Fitness Değeri: ", zeckTotalFitness)
# print("Nesilde Toplam Fitness Değerinde Sağlanan Artış Oranı : %",(zeckTotalFitness-totalFitness)*100/totalFitness)