basic_pay= float(input("enter your basic salary :"))
if basic_pay<0:
    print("salary cannot be nagative")
#calculate HRA
hra=basic_pay*0.5
print("your hra is",hra)
#CALCULATE TA
ta=basic_pay*0.10
print("your ta is",ta)
#calculate professional tax
pt=basic_pay*0.2
print("your professional tax is",pt)
#calculate total salry
tsal=basic_pay=hra+ta-pt
print("your total salary is;",tsal)