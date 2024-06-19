def p(j1,j2):
    max1,max2,fill=3,4,2
    print("%d\t%d"%(j1,j2))
    if j2 is fill:
        return
    elif j2 is max2:
        p(0,j1)
    elif j1!=0 and j2 is 0:
        p(0,j1)
    elif j1 is fill:
        p(j1,0)
    elif j1 < max1:
        p(max1,j2)
    elif j1 < (max2-j2):
        p(0,(j1+j2))
    else:
        p(j1-(max2-j2),(max2-j2)+j2)
        
print("j1\tj2")
p(0,0)
