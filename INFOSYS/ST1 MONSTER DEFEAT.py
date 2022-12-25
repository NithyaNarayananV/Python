'''
Samples of Infosys Online Test

Sample Test 1
While playing an RPG game, you were assigned to complete one of the hardest quests in this game.
There are n monsters you'll need to defeat in this quest. Each monster i is described with two integer
numbers - poweri and bonusi. To defeat this monster, you'll need at least poweri experience points. If
you try fighting this monster without having enough experience points, you lose immediately. You will
also gain bonusi experience points if you defeat this monster. You can defeat monsters in any order.
The quest turned out to be very hard - you try to defeat the monsters but keep losing repeatedly. Your
friend told you that this quest is impossible to complete. Knowing that, you're interested, what is the
maximum possible number of monsters you can defeat? (Question difficulty level: Hardest)
Input:
The first line contains an integer, n, denoting the number of monsters.
The next line contains an integer, e, denoting your initial experience.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, poweri, which represents
power of the corresponding monster.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, bonusi, which represents
bonus for defeating the corresponding monster.
Sample cases:
Input Output Output description
2
123
78
130
10
0

2 Initial experience level is 123 points.

Defeat the first monster having power of 78 and bonus of 10.
Experience level is now 123+10=133.
Defeat the second monster.

3
100
101
100
304
100
1
524

2 Initial experience level is 100 points.

Defeat the second monster having power of 100 and bonus of 1.
Experience level is now 100+1=101.
Defeat the first monster having power of 101 and bonus of 100.
Experience level is now 101+100=201.
The third monster can't be defeated.

// SELF Input
6
50
60
150
80
365
302
30
1
60
100
60
30
50


OUTPUT : 4
'''
n=int(input())
e=int(input())

P=[]
B=[]
for i in range (n):
    power=int(input())
    P.append(power)
for i in range(n):
    bonus=int(input())    
    B.append(bonus)
s=e+sum(B)
defeat=0
#print('Sum ' ,s)
print("Monster's Count   : ",n)

print('Power : ',P)
print('Bonus : ',B)
print("\nInitial Energy  : ",e)
i=0
k=n
w=0
while(k>0):
    #print(' P: ',k,P)
    #print(' B: ',k,B)
    '''
    w=w+1
    if w>5:
        break
    '''
    for j in range(0,n,1):
        if(P[j]>(s-B[j])):
            #print('78 ',P[j],s-B[j])
            print('\nPower - ',P[j],'| Energy -',e)
            print("UNABLE TO DEFEAT")
            P[j]=0
            k=k-1
            s=s-B[j]
            B[j]=0
            continue
        elif P[j]==0:
            continue
        elif P[j]<=e:
            print('\nPower - ',P[j],'| Energy -',e)
            
            e=e+B[j]
            P[j]=0
            k=k-1
            defeat=defeat+1
            print("Current Energy : ",e)
            print("DEFEATED")
            break
#print(e)
print('\nTOTAL DEFEAT : ',defeat)            

'''
INPUT 
6
50
60
150
80
365
302
30
1
60
100
60
30
50
 
OUTPUT
Monster's Count   :  6
Power :  [60, 150, 80, 365, 302, 30]
Bonus :  [1, 60, 100, 60, 30, 50]

Initial Energy  :  50

Power -  365 | Energy - 50
UNABLE TO DEFEAT

Power -  302 | Energy - 50
UNABLE TO DEFEAT

Power -  30 | Energy - 50
Current Energy :  100
DEFEATED

Power -  60 | Energy - 100
Current Energy :  101
DEFEATED

Power -  80 | Energy - 101
Current Energy :  201
DEFEATED

Power -  150 | Energy - 201
Current Energy :  261
DEFEATED

TOTAL DEFEAT :  4
'''

