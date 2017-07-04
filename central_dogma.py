# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:22:25 2016

@author: Joshua
"""

#Function to import DNA file
def DNA_import ():
    file_name = input('Enter the DNA sequence file name without file type (ex: no .txt):')
    file_type = input('Enter the file type (ex: .txt):')
    sequence_file = file_name + file_type
    myfile = open(sequence_file,'r')
    sequence_function = myfile.read()
    sequence_main = ''
    sequence_main = sequence_function
    return sequence_main
#Function to transcribe DNA
def transcription(DNA_main):
    RNA_function = ''
    base = ''
    n = len(DNA_main)
    for i in range(0, n):
        if DNA_main[i] == 'G':
            base = 'G'
            RNA_function = RNA_function + base
            continue
        if DNA_main[i] == 'C':
            base = 'C'
            RNA_function = RNA_function + base
            continue
        if DNA_main[i] == 'T':
            base = 'U'
            RNA_function = RNA_function + base
            continue
        if DNA_main[i] == 'A':
            base = 'A'
            RNA_function = RNA_function + base
            continue
    return RNA_function
#Function to translate RNA
def translation(RNA_main):
    i = 0
    n = len(RNA_main)
    peptide = ''
    Protein_function = ''
    codon = ''
    for i in range(0,n):
        codon = RNA_main[i:i+3]
        if codon == 'AUG':
            RNA_main = RNA_main[i:n]
            break
        else:
            continue
    n = len(RNA_main)
    if RNA_main[0:3] != 'AUG':
        Protein_function = 'X'
    for i in range(0,n,3):
        codon = RNA_main[i:i+3]
        if codon == 'AUG':
            peptide = 'M'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('GCU', 'GCC', 'GCA','GCG'):
            peptide = 'A'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('CGU', 'CGC', 'CGS', 'CGG', 'CGG', 'AGA', 'AGG'):
            peptide = 'R'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('AAU', 'AAC'):
            peptide = 'N'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('GAU', 'GAC'):
            peptide = 'D'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('UGU', 'UGC'):
            peptide = 'Q'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('GAA', 'GAG'):
            peptide = 'E'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('GGU', 'GGC', 'GGA', 'GGG'):
            peptide = 'G'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('CAU', 'CAC'):
            peptide = 'H'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('AUU', 'AUC', 'AUA'):
            peptide = 'I'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'):
            peptide = 'L'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('AAA', 'AAG'):
            peptide = 'K'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('CCU', 'CCC', 'CCA', 'CCG'):
            peptide = 'P'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('ACU', 'ACC', 'ACA'):
            peptide = 'T'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('UGG'):
            peptide = 'W'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('GUU', 'GUC', 'GUA', 'GUG'):
            peptide = 'V'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('UAU', 'UAC'):
            peptide = 'Y'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'):
            peptide = 'S'
            Protein_function = Protein_function + peptide
            continue
        if codon in ('UAA', 'UGA', 'UAG'):
            break
        if codon in ('UUU', 'UUC'):
            peptide = 'F'
            Protein_function = Protein_function + peptide
            continue     
    if Protein_function[0] == 'X':
        Protein_function = 'Untranslatable'
    return Protein_function

#Program testing

#Importing DNA
#DNA = DNA_import()
#Define variable as function, makes variable the 'return' value
#print('DNA sequence from file: %s' %DNA)
#Transcription
#RNA = transcription(DNA)
#print('RNA transcript: %s' %RNA)
#Protein = translation(RNA)
#print('Protein translated from file: %s' %Protein) 
        