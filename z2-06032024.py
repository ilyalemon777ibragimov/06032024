s12 = 0
for x in range(0,8):
    a = 8*16**4+5*16**3+6*16**2+9*16**1+x*16**0
    b = 1*16**4+2*16**3+x*16**2+4*16**1+8*16**0
    s = a+b
    
    print(s) 
    s8 = oct(s)     
    print(s8)
