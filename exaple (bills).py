ncm=int(input("enter the numbre of customers :")) #the number of customers
name=[]
nc=[] #Number of aticles
for i in range(ncm):
    fn=input("enter the full name:") #fn=full name
    name.append(name)
    ni=int(input("enter the number of article:")) #ni=number of items
    nc.append(ni)
tp=[] #tp=Total Payable
t=0 #t=total
for i in range(ni):
    fp=float(input("enter the initial price:"))
    while fp<=0:
        fp=float(input("the value incorrect,try again:"))
    ttc=fp*(1+15/100)
    total=ttc-ttc*(2/100)
    tp.append(total)
for i in range(ncm):
    print("the total biil for the customer ",name," is:",tp)

