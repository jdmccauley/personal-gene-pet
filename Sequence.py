# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:35:31 2016

@author: Joshua
"""
#Note: Hold fn and push F9 to run current line

#This is to be a program that:
#1.Takes in a DNA sequence
#2.Outputs RNA sequence
#3.Outputs Amino Acid Sequence.

filename = input('Enter the DNA sequence file name without file type (ex: no .txt):');
filetype = input('Enter the file type (ex: .txt):');
sequence_file = filename + filetype
myfile = open(sequence_file,'r')
sequence = myfile.read()
print('DNA sequence from file: %s' %sequence)

n = len(sequence)
codon = ''
codons = ''
i = 0
for i in range(0,n,3):
    codon = sequence[i:i+3]
    codons = codons + codon

i = 0
#Now to make the mRNA.
#Note: Coding strand is actually the complement to the template strand.
#mRNA is the complement of template strand, so mRNA looks like coding strand.
RNA = ''
base = ''
for i in range(0,n):
    if codons[i] == 'G':
        base = 'G'
        RNA = RNA + base
        continue
    if codons[i] == 'C':
        base = 'C'
        RNA = RNA + base
        continue
    if codons[i] == 'T':
        base = 'U'
        RNA = RNA + base
        continue
    if codons[i] == 'A':
        base = 'A'
        RNA = RNA + base
        continue
print('Transcribed DNA to RNA: %s' %RNA)
#RNA is made
#Now to translate

i = 0
peptide = ''
Protein = ''
codon = ''
for i in range(0,n,3):
    codon = RNA[i:i+3]
    if codon == 'AUG':
        peptide = 'M'
        Protein = Protein + peptide
        continue
    if codon in ('GCU', 'GCC', 'GCA','GCG'):
        peptide = 'A'
        Protein = Protein + peptide
        continue
    if codon in ('CGU', 'CGC', 'CGS', 'CGG', 'CGG', 'AGA', 'AGG'):
        peptide = 'R'
        Protein = Protein + peptide
        continue
    if codon in ('AAU', 'AAC'):
        peptide = 'N'
        Protein = Protein + peptide
        continue
    if codon in ('GAU', 'GAC'):
        peptide = 'D'
        Protein = Protein + peptide
        continue
    if codon in ('UGU', 'UGC'):
        peptide = 'Q'
        Protein = Protein + peptide
        continue
    if codon in ('GAA', 'GAG'):
        peptide = 'E'
        Protein = Protein + peptide
        continue
    if codon in ('GGU', 'GGC', 'GGA', 'GGG'):
        peptide = 'G'
        Protein = Protein + peptide
        continue
    if codon in ('CAU', 'CAC'):
        peptide = 'H'
        Protein = Protein + peptide
        continue
    if codon in ('AUU', 'AUC', 'AUA'):
        peptide = 'I'
        Protein = Protein + peptide
        continue
    if codon in ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'):
        peptide = 'L'
        Protein = Protein + peptide
        continue
    if codon in ('AAA', 'AAG'):
        peptide = 'K'
        Protein = Protein + peptide
        continue
    if codon in ('CCU', 'CCC', 'CCA', 'CCG'):
        peptide = 'P'
        Protein = Protein + peptide
        continue
    if codon in ('ACU', 'ACC', 'ACA'):
        peptide = 'T'
        Protein = Protein + peptide
        continue
    if codon in ('UGG'):
        peptide = 'W'
        Protein = Protein + peptide
        continue
    if codon in ('GUU', 'GUC', 'GUA', 'GUG'):
        peptide = 'V'
        Protein = Protein + peptide
        continue
    if codon in ('UAU', 'UAC'):
        peptide = 'Y'
        Protein = Protein + peptide
        continue
    if codon in ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'):
        peptide = 'S'
        Protein = Protein + peptide
        continue
    if codon in ('UAA', 'UGA', 'UAG'):
        break
    if codon in ('UUU', 'UUC'):
        peptide = 'F'
        Protein = Protein + peptide
        continue
if Protein[0] != 'M':
    print('mRNA does not have start codon. Cannot translate DNA sequence.')
else: 
    print('Translated Protein sequence: %s' %Protein)
        