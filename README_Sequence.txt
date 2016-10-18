README for Sequence.py

This program is used for transcription and translation of a DNA sequence taken from a .txt file that only contains a sequence containing 'G', 'C', 'A', and 'T'.

First you enter the .txt tile name, such as 'sequence' minus the .txt.

Then you enter the file type, such as '.txt' or '.fasta'.

The text sequence is then read into a string, as a DNA sequence. 

To transcribe the DNA, the sequence string is modified into a new string of RNA, where the 'T' is replaced with 'U'. The sequence string is parsed though and added to a new string, with the 'T' being replaced with 'U'.

To translate the RNA, the RNA sequence is parsed through as strings of three characters. Using the Genetic Code of Life, the 3 character strings are seen as 'codons', and each codon is assigned an Amino Acid. If a 'stop codon' is reached, the translation algorithm is terminated, as does in RNA translation in a cell.

After translation, the translated peptide (sequence of amino acids) product is tested. If the peptide does not start with Methionine, the first Amino Acid in any translation product, the peptide is not read out because the DNA sequence did not code for Methionine.