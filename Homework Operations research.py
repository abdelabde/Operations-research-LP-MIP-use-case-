'''Problem1'''

'''a-Formulating a linear programming model:
    Variables:
        x:number of wood-framed windows
        y:number of aluminum-framed windows
    Max   Z=300*x+180*y
    S.t  6*x+8*y<=48 (1)
          x <=6 (2)
          y <=5 (3)'''
          
'''d-Solving the problem using python'''
import  pulp
problem  =  pulp .LpProblem ("MIP" ,  pulp . LpMaximize )
'''Variables'''
x=[pulp . LpVariable ('x' + str(i) ,cat='Integer' )for i in range(2)]
'''Objective function'''
L1=[300,180]
problem += pulp . lpSum (x[i]*L1[i] for i in range(2))
''' Constraints'''
L2=[6,8]
problem +=pulp . lpSum(x[i]*L2[i] for i in range(2))<=48
L3=[7,5]
for j in range(2):
    problem +=x[j]<=L3[j]
print(problem.solve())
'''print(problem.solve()) returns 1 which means the problem has an optimal solution'''
L4=[] #list variables soltions
for i in  range (2):
    L4.append(pulp . value (x [i]))
print(L4)
'''The optimal soltuion is to produce:
    6:wood-framed windows  and 1 alimunium-framed windows'''
print(pulp . value ( problem . objective ))
'''The line above returns the total profit per day that the company will gain'''
'''e- What constraints are binding? Interpret the shadow price value of each constraint:
    the variable values that gives optimal solution are:
        wood-framed windows:6
        alimunium-framed windows:1
    So, as we replace these values in the linear programming model in the question a we 
    remark that the second constraint (2) is the only binding constrainte(the right side equal to the left side)
    Shadow price value interpretation:
        (1)First constraint: if we increase the right side of the constraint with 1 unit the objective function will not change
        (2)Second constraint: if we increase the right side of the constraint with 1 unit the objective function will increase by 120
        (3)third constraint: if we increase the right side of the constraint with 1 unit the objective function will will not change'''
'''f-How the optimal solution would be change?
    We will use the same problem formulated above in question d just change 300 by 200 as follows:'''
    
problem  =  pulp .LpProblem ("MIP" ,  pulp . LpMaximize )
'''Variables'''
x=[pulp . LpVariable ('x' + str(i) ,cat='Integer' )for i in range(2)]
'''Objective function'''
L1=[200,180]
problem += pulp . lpSum (x[i]*L1[i] for i in range(2))
'''Logical Constraints'''
L2=[6,8]
problem +=pulp . lpSum(x[i]*L2[i] for i in range(2))==48
L3=[6,5]
for j in range(2):
    problem +=x[j]<=L3[j]
print(problem.solve())
'''print(problem.solve()) returns 1 which means the problem has an optimal solution'''
L4=[] #list variables soltions
for i in  range (2):
    L4.append(pulp . value (x [i]))
print(L4)
'''The optimal soltuion is to produce always:
    4:wood-framed windows  and 3 alimunium-framed windows'''
'''g-the change on the optimal solution if Doug lowered his working hours '''
problem  =  pulp .LpProblem ("MIP" ,  pulp . LpMaximize )
'''Variables'''
x=[pulp . LpVariable ('x' + str(i) ,cat='Integer' )for i in range(2)]
'''Objective function'''
L1=[300,180]
problem += pulp . lpSum (x[i]*L1[i] for i in range(2))
'''Logical Constraints'''
L2=[6,8]
problem +=pulp . lpSum(x[i]*L2[i] for i in range(2))==48
L3=[5,5]
for j in range(2):
    problem +=x[j]<=L3[j]
print(problem.solve())
'''print(problem.solve()) returns 1 which means the problem has an optimal solution'''
L4=[] #list variables soltions
for i in  range (2):
    L4.append(pulp . value (x [i]))
print(L4)

'''There would be no change on the optimal solution because resolving the problem
 gives 4 wood-framed windows and 3 aliminium-framed windows'''
 
'''Problem two'''
''''a-Report the optimal solution for decision variables and the objective value''' 
problem  =  pulp .LpProblem ("MIP" ,  pulp . LpMinimize )
'''Variables'''
x=[pulp . LpVariable ('x' + str(i) ,cat='LpContinuous' )for i in range(3)]
'''Objective function'''
L1=[3,3,5]
problem += pulp . lpSum (x[i]*L1[i] for i in range(3))
'''Logical Constraints'''
L2=[2,0,1]
problem +=pulp . lpSum(x[i]*L2[i] for i in range(3))>=8
L3=[0,1,1]
problem +=pulp . lpSum(x[i]*L3[i] for i in range(3))>=6
L4=[6,8,0]
problem +=pulp . lpSum(x[i]*L4[i] for i in range(3))>=48
for j in range(3):
    problem +=x[j]>=0
print(problem.solve())
'''print(problem.solve()) returns 1 which means the problem has an optimal solution'''
L5=[] #list variables soltions
for i in  range (3):
    L5.append(pulp . value (x [i]))
print(L5)
'''The optimal soltuion is as follows:
   x1=4,x2=6,x3=0'''
print(pulp . value ( problem . objective ))
'''The value of objective function is 30'''
'''b-Report and interpret the reduced cost1 value of each decision variable. 
    For the first decison variable,its associated coefficient is poistive so if we increase this variable by one unit the objective function will increase by 
    3 ,and the same for the second decision variable but for the third decision variable the increase by one unit will cause an increase of the objective function by 5'''
 
'''Problem three'''
'''a-Formulate an LP model and implement it in Python:
    Variables:
        x1:The amount of money to be invested in Bonds A
        x2:The amount of money to be invested in Bonds B
        x3:The amount of money to be invested in Bonds C
        x4:The amount of money to be invested in Bonds D
        x5:The amount of money to be invested in Bonds E
        
    Max   Z=0.095*x1+0.08*x2+0.09*x3+0.09*x3+0.09*x4+0.09*x5
constraintes :
              x2+x5>=0.5*500000
              x1+x4+x5<=0.5*500000
              x1+x2+x4>=0.3*500000
              x1+x2+x3+x4+x5=500000'''
              
'''Python Implementation'''
problem1  =  pulp .LpProblem ("MIP" ,  pulp . LpMaximize )
'''Variables'''
x=[pulp . LpVariable ('x' + str(i) ,cat='LpContinuous' )for i in range(5)]
'''Objective function'''
L1=[0.095,0.08,0.09,0.09,0.09]
problem1 += pulp . lpSum (x[i]*L1[i] for i in range(5))
''' Constraints'''
L2=[0,1,0,0,1]
problem1 +=pulp . lpSum(x[i]*L2[i] for i in range(5))>=0.5*500000
L3=[1,0,0,1,1]
problem1 +=pulp . lpSum(x[i]*L3[i] for i in range(5))<=0.5*500000
L4=[1,1,0,1,0]
problem1 +=pulp . lpSum(x[i]*L4[i] for i in range(5))>=0.3*500000
problem1 +=pulp . lpSum(x[i] for i in range(5))==500000
print(problem1.solve())
'''print(problem.solve()) returns 1 which means the problem has an optimal solution'''
L5=[] #list variables soltions
for i in  range (5):
    L5.append(pulp . value (x [i]))
print(L5)
'''L5=[75000.0, 75000.0, 175000.0, 0.0, 175000.0]'''
'''b-The optimal soltuion is as follows:
    75000.0 as an amount in the bonds A
    75000.0 as an amount in the bonds B
    175000.0 as an amount in the bonds C
    0 as an amount in the bonds D
    175000.0 as an amount in the bonds E
   '''
'''b- What constraints are binding? Interpret the shadow prices 
     So,replacing optimal variables values in the linear model of question a we observe that the three constraintes are 
     binding ones (right side equal to the left one)
     
     Shadow price Interpretation:
         
      
   '''
'''c-Interpret the reduced cost value of each decision variable:
    for each decision variable each increase of 1 unit will cause an increase of the objective function by annual return corresponding to the bonds ctegory
    for example for bond A ,an increase of 1 unit of its value will increase the objective function (the profit) by 0.095
          
   '''
'''Problem four'''
'''a- Formulate an Integer LP model for this problem. '''
''':Variables:
        x(i,j):number of tons to be delivered to distributor i from plant j
        i belongs to [Miami,Orlando,Tallahassee ]===>[0,1,2]
        j belonfs to [Eustis,Clermont]===>[0,1]
        
    Min   Z=x(0,0)*260+x(0,1)*220+x(1,0)*220+x(1,1)*240+x(2,0)*290+x(2,1)*320
constraintes :
              x(0,0)+x(0,1)=10
              x(1,0)+x(1,1)=15
              x(2,0)+x(2,1)=10
              x(0,0)+x(1,0)+x(2,0)<=20
              x(0,1)+x(1,1)+x(2,1)<=20
              x(i,j)>=0
              
             '''
             
'''b-Python Implementation and optimal solution''''
problem  =  pulp .LpProblem ("MIP" ,  pulp . LpMinimize )
'''Variables'''
x=[[pulp . LpVariable ('x' + str(i)+str(j),cat='Integer' )for i in range(2)]for j in range(3)]
'''Objective function'''
D={0:[260,220],1:[220,240],2:[290,320]}
problem += pulp . lpSum (x[i][j]*D[i][j] for i in range(3) for j in range(2))
''' Constraints'''
L1=[10,15,10]
for i in range(3):
    problem +=pulp . lpSum(x[i][j] for j in range(2))==L1[i]
for j in range(2):
    problem +=pulp . lpSum(x[i][j] for i in range(3))<=20
for i in range(3):
    for j in range(2):
        problem +=x[i][j]>=0
print(problem.solve())
'''print(problem.solve()) returns 1 which means the problem has an optimal solution'''
D1={} #list variables soltions
for i in  range (3):
    L2=[]
    for j in range(2):
        L2.append(pulp . value (x [i][j]))
    D1[i]=L2
print(D1)
'''After resolving the problem the optimal solution is as follows:
    {0: [0.0, 10.0], 1: [10.0, 5.0], 2: [10.0, 0.0]}
    Which means for:
    Miami:10 tons from  Clermont plant
    Orlando:10 tons from eustis and 5 tons from Clermont plant
    Tallahassee:10 tons from eustis plant '''
    
    
'''Problem five'''
'''a- Formulate a binary LP integer programming this problem. '''
''':Variables:
        x(i,j): 1 if person i handeled the task j
                0 if not 
                i belongs to [Eve,Steven]===>[0,1]
                j belongs to [shpping,cooking,dishwashing,Laundry]===>[0,1,2,3]
        
    Min   Z=x(0,0)*4.5+x(0,1)*7.5+x(0,2)*3.5+x(0,3)*3+x(1,0)*5+x(1,1)*7.2+x(1,2)*4.5+x(1,3)*3.2
constraintes :
              x(0,0)+x(0,1)+x(0,2)+x(0,3)=2
              x(1,0)+x(1,1)+x(1,2)+x(1,3)=2
              x(0,0)+x(1,0)=1
              x(0,1)+x(1,1)=1 
              x(0,2)+x(1,2)=1 
              x(0,3)+x(1,3)=1 
             '''
'''b-Python Implementation and optimal solution''''
problem  =  pulp .LpProblem ("MIP" ,  pulp . LpMinimize )
'''Variables'''
x=[[pulp . LpVariable ('x' + str(i)+str(j),cat='Binary' )for j in range(4)]for i in range(2)]
'''Objective function'''
D={0:[4.5,7.5,3.5,3],1:[5,7.2,4.5,3.2]}
problem += pulp . lpSum (x[i][j]*D[i][j] for i in range(2) for j in range(4))
''' Constraints'''
for i in range(2):
    problem +=pulp . lpSum(x[i][j] for j in range(4))==2
for j in range(4):
    problem +=pulp . lpSum(x[i][j] for i in range(2))==1
print(problem.solve())
'''print(problem.solve()) returns 1 which means the problem has an optimal solution'''
D1={} #list variables soltions
for i in  range (2):
    L2=[]
    for j in range(4):
        L2.append(pulp . value (x [i][j]))
    D1[i]=L2
print(D1)
'''After resolving the problem the optimal solution is as follows:
    {0: [1.0, 0.0, 1.0, 0.0], 1: [0.0, 1.0, 0.0, 1.0]}
    Which means for:
    Eve:will take Shopping and Dishwasing
    Qteven:will take coking and Laundry  '''
    
'''Problem six'''

''' Formulating a MIP (Mixed Integer Programming) model for this problem'''
''':Variables:
        x1:the number of toys 1 to be produced 
        x2:the number of toys 2 to be produced
        y1:Binary,1:if the toys will be produced in factory 1
                  0 :if not
        y2:Binary,1:if the toys will be produced in factory 2
                  0 :if not
        
    Max   Z=x1*10+x2*15
constraintes :
              x1<=50*500*y1+40*700*y2
              x2<=40*500*y1+25*700*y2
              y1+y2=1
              0<=x1
              0<=x2 
             '''
'''b-Python Implementation and solving the problem'''

problem  =  pulp .LpProblem ("MIP" ,  pulp . LpMaximize )
'''Variables'''
x=[pulp . LpVariable ('x' + str(i),cat='Integer' )for i in range(2)]
y=[pulp . LpVariable ('y' + str(j),cat='Binary' )for j in range(2)]
'''Objective function'''
L1=[10,15]
problem += pulp . lpSum (x[i]*L1[i] for i in range(2))
''' Constraints'''
problem +=x[0]-50*500*y[0]+40*700*y[1]<=0
problem +=x[1]-40*500*y[0]+25*700*y[1]<=0
problem +=y[0]+y[1]==1
for i in range(2):
    problem +=x[i]>=0
print(problem.solve())
'''print(problem.solve()) returns 1 which means the problem has an optimal solution'''
 #list variables soltions
L2=[]
L3=[]
for i in  range (2):
    L2.append(pulp . value (x [i]))
    L3.append(pulp . value (y [i]))
print(L2)
'''L2=[25000.0, 20000.0]'''
print(L3)
'''L3=[1.0, 0.0]'''
'''After resolving the problem the optimal solution is as follows:
    The toys will be produced in the factory 1
    the optimal number of toys 1 is 25000
    the optimal number of toys 2 is 20000'''




    

    
    '