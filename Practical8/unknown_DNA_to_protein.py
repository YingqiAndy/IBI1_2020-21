#DNA to protein convertor
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

#et gene sequences of unknown function in fasta format
#Import toolkits needed
import re
#the input
newfile = input('filename:')
#read the infile and creat the outfile
infile=open(newfile,'r')
outfile=open('protein.fa','w')
#extract sequence of the specfic gene
for line in infile:
    if line.startswith('>'):
        name = re.findall(r'>(\S+)', line)   #extract names of gene
# extract sequence of genes that unknown function
        seq = ''
        line=next(infile,'0')
        seq=line.replace('\n', '')
        f = '>' + name[0]  # creat a variable to show the name and length of genes
# search the start sit
        start_sit = re.search('ATG', seq)
        protein = ''

# Correlate codon to protein
        for i in range( start_sit.start(), len(seq), 3):

            if (table[seq[i:i + 3]] == 'O') or (table[seq[i:i + 3]] == 'X') or (table[seq[i:i + 3]] == 'U'):
                break
            else:
                protein += table[seq[i:i + 3]]

#write the outfile
        outfile.write(f'{f:30}')
        outfile.write(('length: '+str(int(len(seq)/3))))
        outfile.write(('\n'))
        outfile.write(protein)
        outfile.write('\n')
#store the infile and outfile
outfile.close()
infile.close()





