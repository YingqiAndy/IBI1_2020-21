#3.1 Some simple math
a = 130302
b = 190784
c = 100321
d=abs(a-c)
e=abs(a-b)
if d<e:
    print("d<e")
else:
    print("d>=e")

#3.2 Booleans
X = True
Y = False
Z = (X and not Y) or (Y and not X)
if Z == True:
    print("True")
else:
    print("False")

W = (X!=Y)
if Z == W:
    print("Z == W")
else:
    print("Z != W")