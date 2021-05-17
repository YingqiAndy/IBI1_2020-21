#List manipulation
import matplotlib.pyplot as plt
import numpy as np
#Setting Initial Values
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts=np.array([51,1142,42,216,25,650,32533,57,1,523])

# average length

average_length = gene_lengths/ exon_counts
average_length.sort()  #Sort the average length of exons from small to large
print(average_length)  #show the sorted length
#boxplot
#Set the details of the graphics
plt.boxplot(average_length,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline = False,
            showbox= True,
            showcaps = True,
            showfliers = True,
            notch= False,
            )
plt.title('exon length')
plt.show()  #show the boxplot