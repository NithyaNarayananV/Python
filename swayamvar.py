'''
Example 1

Input
4
rrmm mrmr

Output
0


Example 2

Input
4 rmrm mmmr

Output
2

Example 3 Mine

Input
5 rrmrm mrmrm

Output
1
'''


Input=int(input())
Tot_Pairs=int(Input)
L=Tot_Pairs
BrideInput=input()
GroomInput=input()
#Bride=[]
#Groom=[]
R=0
G=0
for i in range (Tot_Pairs):
    if GroomInput[i] == 'r':
        R=R+1
    if BrideInput[i] == 'm':
        G=G+1
for i in range(Tot_Pairs):
    if BrideInput[i] == 'r':
        if R == 0 :
            break
        R=R-1
        L = L - 1
    if BrideInput[i] == 'm':
        if G == 0 :
            break
        G=G-1
        L = L - 1
print(L)

