# R rate
n=84 #the number of IBI1 students
r=1.2 #R rate
for i in range(0,5):
    c=n*r #The number of new infections in a round
    n=n+c #The total number of people infected after each round

print("R rate is "+ str(r) + " and the total number of individuals infected after 5 generations is " + str(n))