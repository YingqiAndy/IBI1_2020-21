#DNA to protein convertor
#Import toolkits needed
import re

seq ='ATGCGACTACGATCGAGGGCC'       #create the string variable seq
#Create a codon subdirectory
table = {
        'ATA': 'J', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'B', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Z',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': 'O', 'TAG': 'U',
        'TGC': 'C', 'TGT': 'C', 'TGA': 'X', 'TGG': 'W'}
start_sit = re.search('ATG', seq)  #search the start sit
protein=''
#Correlate codon to protein
for i in range(start_sit.end() - 3, len(seq), 3):
        protein += table[seq[i:i + 3]]
        if (table[seq[i:i + 3]] == 'O') or (table[seq[i:i + 3]] == 'X')or (table[seq[i:i + 3]] == 'U'):
            break
print(protein) #output proteins

