s12 = 0
for x in range(0,12):
    a = 5*16**4+7*16**3+10*16**2+x*16**1+9*16**0
    b = 5*8**2+4*8**1+x*8**0
    s = a*b
    
    print(s) 
    print(s12)
    s12 = 0
    while s>0:
        s = s//12
        s12 += s%12
    print(s12)



