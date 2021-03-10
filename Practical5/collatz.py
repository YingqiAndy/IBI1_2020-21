#4 Fibonacci sequence
a=1
b=1
# set the first two digits
print(a) #output the first digit
# get the 13th digit
for i in range(1,13): # Repeat 12 more cycles
    c=a+b # Generate C(n+1) for the next digit
    a=b
    b=c
#Recursive calculation
    print(a) # get the next digit