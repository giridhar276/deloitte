#list
alist = [10,20,30]
alist[0] = 100
print(alist)

'''
#tuple
atup = (10,20,30)
atup[0] = 100
print(atup)
'''

# elements inside tuple cannot be modified directly but we make changes by typecasting
atup = (10,20,30)    # tuple

alist = list(atup)   # converting to list
alist.append(50)     # making changes
atup = tuple(alist)  # reconverting to tuple
print(atup)

#list of lists
empdb = [["rita","sharma",12345,"RFDF34"],["gita","singh",575645,"UYRJF"]]
#list of tuples
empdb = [("rita","sharma",12345,"RFDF34"),("gita","singh",575645,"UYRJF")]
