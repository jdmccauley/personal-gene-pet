# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:44:20 2016

@author: Joshua
"""
def mutation(DNA,mutagen):
    import random
    length = len(DNA)
    mutagen = int(mutagen)
    DNA_list = list(DNA)
    #must make string a list in order to edit
    for i in range(0,mutagen):
        p = random.random()
        n = p * length
        correction = n % 1
        n = n - correction
        n = int(n)
        change = random.random()
        if DNA_list[n] == 'G':
            if change <= 0.33:
                DNA_list[n] = 'C'
            if 0.33 < change <= 0.66:
                DNA_list[n]  = 'A'
            if 0.66 < change:
                DNA_list[n] = 'T'
            continue
        if DNA_list[n] == 'C':
            if change <= 0.33:
                DNA_list[n] = 'G'
            if 0.33 < change <= 0.66:
                DNA_list[n]  = 'A'
            if 0.66 < change:
                DNA_list[n] = 'T'
            continue
        if DNA_list[n] == 'A':
            if change <= 0.33:
                DNA_list[n] = 'C'
            if 0.33 < change <= 0.66:
                DNA_list[n] = 'G'
            if 0.66 < change:
                    DNA_list[n] = 'T'
            continue
        if DNA_list[n] == 'T':
            if change <= 0.33:
                DNA_list[n] = 'C'
            if 0.33 < change <= 0.66:
                DNA_list[n] = 'A'
            if 0.66 < change:
                DNA_list[n] = 'G'
            continue
    DNA_mutated = ''.join(DNA_list)
    return DNA_mutated