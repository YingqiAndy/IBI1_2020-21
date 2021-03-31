#et gene sequences of unknown function in fasta format
#Import toolkits needed
import re
#read the infile and creat the outfile
infile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
outfile=open('unknown_function.fa','w')
#creat a cycle for extracting specfic data
#extract names of genes
for line in infile:
    if line.startswith('>'):
        if re.search(r'unknown function',line):
            name= re.findall(r'gene:(.+?)\s',line)

            #extract sequence of genes that unknown function
            seq =''
            while True:
                line =next(infile)
                if line.startswith('>'):
                    break
                line2=line.replace('\n','')

                seq =seq + line2           #the sequence of genes that unknown function
            f ='>' + name[0]             #creat a variable to show the name and length of genes
            #write the outfile
            outfile.write(f'{f:30}')
            outfile.write(('length: '+str(int(len(seq)))))
            outfile.write(('\n'))
            outfile.write(seq)
            outfile.write('\n')

#store the infile and outfile
outfile.close()
infile.close()





