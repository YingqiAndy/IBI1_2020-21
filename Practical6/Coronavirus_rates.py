#Comparing coronavirus infection rates across countries
import matplotlib.pyplot as plt
import numpy as np
#Setting Initial Values
Country = ['USA', 'India','Brazil','russia','UK']
Cases = [29862124,11285561,11205972,4360823,4232924]
total = 0     #Set initial value
frequency = []
for i in Cases:
    total += i       # output the number of total cases
for x in Cases:
    frequency.append(float(x)/total)     #output 5 frequency
frequencydictionary = dict(zip(Country,frequency))  #Combined to generate frequencydictionary
print(frequencydictionary)


#pie chart
#specifies the fraction of the radius with which to offset each wedge
plt.title('Coronavirus frequency')
plt.pie(frequency, labels=Country, autopct='%1.1f%%',shadow=True, startangle=90)
plt.axis('equal') #Equal aspect ratio ensures that pie is drawn as a circle

plt.show()  # show the pie chart