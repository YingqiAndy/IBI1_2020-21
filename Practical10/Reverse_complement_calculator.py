#Reverse complement calculator
#define the function reverse_complement
def resverse_complement(DNA):
    complement =''             #creat a list to accommodate the sequence
    #creat the complementary dictionary
    complement_dictionary={'A':'T','T':'A','G':'C','C':'G','a':'t','t':'a','g':'c','c':'g'}
    for i in DNA:
        complement += complement_dictionary[i]        #get the complementary sequence
        list1=list(complement)                        #transfer the string to list to reverse the order
        list1.reverse()                               #reverse the order
        reverse_complementary_sequence =''.join(list1)          #join elements together and get the reverse complementary sequence
    return reverse_complementary_sequence
DNA_sequence= input('DNA sequence: ')                   #input initial DNA sequence
print(resverse_complement(DNA_sequence))                #out put the reverse_complementary_sequence