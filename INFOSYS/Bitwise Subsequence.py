'''
Bitwise subsequence
You have an array A of N integers A1 A2 .. An. Find the longest increasing subsequence Ai1 Ai2 .. Ak
(1 <= k <= N) that satisfies the following condition:
For every adjacent pair of numbers of the chosen subsequence Ai[x] and Ai[x+1] (1 < x < k), the 
expression( Ai[x] & Ai[x+1] ) * 2 < ( Ai[x] | Ai[x+1] ) is true
Note: '&' is the bitwise AND operation, ' | ' is the bit-wise OR operation
Input:
The first line contains an integer, N, denoting the number of elements in A.
Each line i of the N subsequent lines (where 0 ≤ i < N) contains an integer describing Ai. 
Sample cases:
Input Output Output description
5
15
6
5
12
1
2 One possible subsequence is:
5 12
6
9
17
2
15
5
2
2 One possible subsequence is:
2 15
7
17
16
12
2
8
17
17 
3 One possible subsequ
'''

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

'''
OUTPUT
Input Array -  [9, 17, 2, 15, 25, 26, 2, 5, 10, 22]
-----------
9
17
   l =  2
-----------
2
15
25
   l =  3
-----------
26
   l =  1
-----------
2
5
10
22
   l =  4
-----------

Max Length of Bitwise subsequence =  4

'''

