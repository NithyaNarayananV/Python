#n=int(input())
n=10
L=[]
L=[9,17,2,15,25,26,2,5,10,22]
l=1
m=1
#for i in range (n):
    #t=int(input())
    #L.append(t)
print('Input Array - ',L)
print('-----------')

f=0
#print('=======')
for i in range(n-1):
    if(L[i]<L[i+1]):
        #print(L[i])
        lhs=L[i]&L[i+1]
        rhs=L[i]|L[i+1]
        #print('   *  ',lhs,rhs)
        if(lhs*2<rhs ):
            if(f==0):
                l=l+1
                print(L[i])
                #print('23 l = ',l)
            else:
                print(L[i])
                if(l>m):
                    m=l
                l=1
                l=l+1
                f=0
                
        else:
            f=1
            print(L[i])
            print('   l = ',l)
            print('-----------')
            if(l>m):
                m=l
                l=1
            l=1
            #print('not',L[i],L[i+1])
            

    else:
        f=1
        print(L[i])
        print('   l = ',l)
        print('-----------')
        if(l>m):
            m=l
        l=1
          
            #print(L[i])
            #print('-----')
print(L[n-1])
print('   l = ',l)
print('-----------')
if(l>m):
    m=l
    l=1

print('Max Length of Bitwise subsequence = ',m)


