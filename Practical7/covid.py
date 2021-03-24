# import python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#change the working directory to full_data.csv
os.chdir("/Users/bob/PycharmProjects/Practical7")
os.getcwd()  #View the current directory
os.listdir()  #View the files in the current directory

#use the pandas library to read the content of the .csv file into a dataframe object
covid_data=pd.read_csv("full_data.csv")
#show the correct code for showing all columns, and every second row between (and
#including) 0 and 10
print(covid_data.iloc[0:10:2,:])
covid_data.info()  #show information of covid_data.csv
covid_data.describe()  #shows the number of entries, mean, standard deviation and a number of quantiles.
#use a Boolean to access entries
#get the data of total_cases in Afghanistan
my_columns = [True, True, False, False, True, False]
total_cases_Afghanistan =[]
for i in range(7996):
    if covid_data.loc[i,"location"]=="Afghanistan":
        total_cases_Afghanistan.append(True)
    else:
        total_cases_Afghanistan.append(False)

print(covid_data.loc[total_cases_Afghanistan,"total_cases"])

#get the data of total new cases in the World
my_columns1 =[True, True, True, False, False, False ]
new_cases_World =[]
for i in range(7996):
    if covid_data.loc[i,"location"]=="World":
        new_cases_World.append(True)
    else:
        new_cases_World.append(False)
world_new_cases=covid_data.loc[new_cases_World,"new_cases"]

print("the mean of new cases for the entire world :",np.mean(world_new_cases))  #output the mean of world new cases
print("the median of new cases for the entire world :",np.median(world_new_cases))   #output the median of world new cases
#created a boxplot of new cases worldwide
#set the content for the boxplot
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline = False,
            showbox= True,
            showcaps = True,
            showfliers = True,
            notch= False,
            )
plt.show()  #show the boxplot of world


#get the data of date and new deaths in the World
world_dates=covid_data.loc[new_cases_World,"date"]
world_new_deaths=covid_data.loc[new_cases_World,"new_deaths"]
#creat a plot including both new cases and new deaths in the world
plt.plot(world_dates, world_new_cases, 'b+')
plt.plot(world_dates, world_new_deaths, 'r+')
plt.title("Total cases and deaths in World")
plt.xlabel("date")
plt.ylabel("number")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.gcf().subplots_adjust(bottom=0.20)
plt.show()  #show the plot

# Answer the question
#get the data of new cases in China
my_columns2 =[True, True, True, False, False, False ]
new_cases_China =[]
for i in range(7996):
    if covid_data.loc[i,"location"]=="China":
        new_cases_China.append(True)
    else:
        new_cases_China.append(False)
China_new_cases=covid_data.loc[new_cases_China,"new_cases"]
#get the data of new cases in Austria
my_columns3 =[True, True, True, False, False, False ]
new_cases_Austria =[]
for i in range(7996):
    if covid_data.loc[i,"location"]=="Austria":
        new_cases_Austria.append(True)
    else:
        new_cases_Austria.append(False)
Austria_new_cases=covid_data.loc[new_cases_Austria,"new_cases"]
#creat the plot of new cases in China and Austria
plt.plot(world_dates, China_new_cases, 'g+')
plt.plot(world_dates, Austria_new_cases, 'y+')
plt.title("The changes of new cases in China and Austria")
plt.xlabel("date")
plt.ylabel("number")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.gcf().subplots_adjust(bottom=0.20) # Modify the size of the plot bottom space
plt.show()  #show the plot