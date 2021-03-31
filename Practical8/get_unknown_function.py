#et gene sequences of unknown function in fasta format
#Import toolkits needed
import re
#read the infile and creat the outfile
infile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
outfile=open('unknown_function.fa','w')
#creat a cycle for extracting specfic data
#extract names of genes
#read the infile
infile1=infile.read()
#Delete all newline characters
infile1=''.join(infile1.split('\n'))
infile1=infile1.replace('\n','')
#extract specific names and sequence
name=re.findall(r'gene:(.+?)\s.*?unknown function',infile1)
seq= re.findall(r'unknown function.*?](.+?)>',infile1)
#write the outfile
for i in range(len(seq)):
    outfile.write(f'>{name[i]:30}length: {len(seq[i])}\n{seq[i]}\n')
#store the infile and outfile
outfile.close()
infile.close()





