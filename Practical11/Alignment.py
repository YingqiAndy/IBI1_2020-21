#Alignment
import re
import os
#read files
humanfile = open('SOD2_human.fa','r')
mousefile = open('SOD2_mouse.fa','r')
randomfile = open('RandomSeq.fa','r')
#creat amino acid list and BLOSUM62 list
amino_acid_list=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*']
BLOSUM62 = [
            [ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
            [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
            [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
            [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
            [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
            [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
            [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
            [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
            [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
            [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
            [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
            [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
            [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
            [ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
            [ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
            [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
            [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
            [ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
            [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
            [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],
]
#define a function to read name and sequence
def read(filename):
    for i in filename:
        if i.startswith('>'):
            name= re.findall(r'>(.*)',i)
            name=name[0]
        else:
            seq=i.strip()

    return name+seq
#define a function to read sequence
def readsequence(filename):

    for i in filename:

        if not i.startswith('>'):
            sequence=i.strip()
    return sequence
#define a function to get the percentage
def percentage(seq1,seq2):
    a = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            a += 1
    percentage = str(a/len(seq1)*100)+'%'
    return percentage
#define a function to get the score
def score(seq1,seq2):
    score=0
    for i in range(len(seq1)):
        location1 = amino_acid_list.index(seq1[i])
        location2 = amino_acid_list.index(seq2[i])
        score1 = BLOSUM62[location1][location2]
        score += score1
    return score
#set variables to storage result from functions
var1 = readsequence(humanfile)
var2 = readsequence(mousefile)
var3 = readsequence(randomfile)

#output results
print('mouse-human:','ppercentage of identical amino acid  = ',percentage(var1,var2),'     score = ',score(var1,var2))
print('random-human:','percentage of identical amino acid = ',percentage(var1,var3),'     score = ',score(var1,var3))
print('mouse-random:','percentage of identical amino acid = ',percentage(var2,var3),'     score = ',score(var2,var3))

#mouse-human: percentage =  89.63963963963964%      score =  1091
#random-human: percentage =  5.405405405405405%      score =  -250
#mouse-random: percentage =  5.8558558558558556%      score =  -250
#The score comparing human SOD2 gene with mouse SOD2 gene is 1091 but both score comparing them with the random sequence are -250. So the mouse SOD2 gene and human SOD2 gene have greater similarity than them with the random sequence. It demonstrates that human SOD2 gene and mouse SOD2 are not random sequences and they have homology.
#The percentage of identical amino acid between human SOD2 gene and mouse SOD2 gene are 89.6% while the random sequence with them are about 5.4% and 5.9%. The percentage of identical amino acid between human SOD2 gene and mouse SOD2 gene is significantly higher, which proved that human SOD2 gene and mouse SOD2 gene have close relationship. We can conclude that humans and mice have partial homology.




