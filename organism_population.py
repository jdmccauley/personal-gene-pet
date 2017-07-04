# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:38:50 2016

@author: Joshua
"""

#Life creation and assignment

import central_dogma
import organism_file_create_temp
import mutation
import os
import random
class organism:
    organism_number = 0
    DNA = ''
    RNA = ''
    Protein = ''
    location = ''
    DNA_length = 0
    selection_value = 0
    survival_prob = 0
n = input('Enter number of organisms to make:')
n = int(n)
j = input('Enter length of DNA for each organism:')
j = int(j)
file_start = '\\organism_'
file_end = '.txt'
population = []
for i in range(0,n):
    org = organism()
    org.organism_number = i
    file_name = file_start + str(i) + file_end
    working_dir = organism_file_create_temp.organism_create(org.organism_number,j)
    org.location = working_dir + file_name 
    organism_file = open(org.location,'r')
    org.DNA = organism_file.read()
    org.RNA = central_dogma.transcription(org.DNA)
    org.Protein = central_dogma.translation(org.RNA)
    organism_file.close()
    population.append(org)
for org in population:
    print('Organism number: %d' %org.organism_number)
    print('Organism Protein: %s' %org.Protein)
#population is made now
#here we create the selection algorithm
generations = input('Enter a number of generations to evolve organisms:')
mutagen = input('Enter a number of mutations to occur:')
adaptation = input('Enter an amino acid sequence to select for:')
x = int(generations)
selected_protein_length = len(adaptation)
probability = input('Enter a perentage of survival for organisms if they do not have the selected amino acid sequence (as percentage such as 55):')
probability = float(probability)
for i in range(0,x):
    for org in population:
        org.selection_value = 0
        for i in range(0,len(org.Protein)):
            if org.Protein[i:i+selected_protein_length] == adaptation:
                org.selection_value = org.selection_value + 1
    #fittest = sorted(population, key=lambda org:org.selection_value, reverse=True)
    fittest = population
    for org in fittest:
        if org.selection_value == 1:
            org.survival_prob = 1.0
        if org.selection_value == 0:
            org.survival_prob = random.random()  
        if org.survival_prob < probability:
            fittest.remove(org)
    for org in fittest:
        print('Organism number: %d' %org.organism_number)
        print('Organism Protein: %s' %org.Protein)
        print('Organism selection value: %d' %org.selection_value)
#organisms are now sorted in fittest list
#need to only take certain amount     
#now for mutation
    for org in fittest:
        org.DNA = mutation.mutation(org.DNA,mutagen)
        new_org_file = open(org.location,'w')
        new_org_file.write(org.DNA)
        new_org_file.close()
        org.RNA = central_dogma.transcription(org.DNA)
        org.Protein = central_dogma.translation(org.RNA)