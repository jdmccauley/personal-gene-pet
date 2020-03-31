# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:35:18 2016

@author: Joshua
"""

#Program to randomly generate DNA files
#Need to create random number generator from 1 to 4
#Assign DNA base to number
#Create string of bases
#When to stop?
#DNA of 1 million is slow to make and trancribe
#But translaiton made an 11 amino acid sequence
#ten thousand bases made one amino acid
#100 thousand made a 15 amino acid protein first 
#Then a 3 amino acid protein
#100 thousand is actually not too slow, and gives a decent amount of variation

def organism_create(organism_number_main,organism_DNA_length_main):
    import random
    import os.path
    working_dir = '/mnt/c/Users/Joshua/Documents/Coding/Projects/Sequence/Organisms'
    #n = input('Enter a number of organisms to be made:')
   # n = int(n)
    organism_DNA_length_main = int(organism_DNA_length_main)
    j = organism_DNA_length_main
    base = ''
    sequence = ''
    file_name_first = 'organism_'
    file_type = '.txt'
    file_number = 0
    file_name = ''
    for i in range(0,j):
        r = random.random()
        if r < 0.25:
            base = 'A'
        if 0.25 <= r < 0.5:
            base = 'G'
        if 0.5 <= r < 0.75:
            base = 'T'
        if 0.75 <=  r <= 1:
            base = 'C'
        sequence = sequence + base
    file_number = organism_number_main
    file_number = str(file_number)
    file_name = file_name_first + file_number + file_type
    total_file_name = os.path.join(working_dir,file_name)
    my_file = open(total_file_name,'w')
    my_file.write(sequence)
    my_file.close()
    return(working_dir)
