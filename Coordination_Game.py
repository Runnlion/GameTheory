#Version Python 3.6.6
#matplotlib required
#Author : Runnlion

import numpy as np
import matplotlib.pyplot as plt

def CoordinationFunction(a,b,c,d,e,f,g,h):
    t = round((g-c)/((a-c-e+g)),3)
    s = round((h-f)/(b+h-f-d),3)
    t1 = []
    s1 = []
    t2 = []
    s2 = []
    x = []
    y = []
    for num in range(0,10001):
        Num = num/10000
        f1 = a*Num + c*(1-Num)
        f2 = e*Num + g*(1-Num)
        f3 = b*Num + f*(1-Num)
        f4 = d*Num + h*(1-Num)
        t1.append(Num)
        s2.append(Num)
        if(f1>f2):
            s1.append(1)
        else:
            s1.append(0)

        if(f3>f4):
            t2.append(1)
        else:
            t2.append(0)
    for num in range(0,10001):
        if((s1[num]==s2[num])&(t1[num]==t2[num])):
            x.append(s1[num])
            y.append(t1[num])
    for num in range(0,10001):
        try:
            if(abs(s1[num]-s1[num+1])==1):
                y.append(t1[num])
        except :
            pass

        try:
            if(abs(t2[num]-t2[num+1])==1):
                x.append(s2[num])
        except :
            pass
    print(x,y)
    plt.title('Recation Function:Battle of Sexes')
    plt.xlabel('s')
    plt.ylabel('t')
    plt.plot(s1,t1)
    plt.plot(s2,t2)
    plt.scatter(x,y)
    print("Nash equilibrium:")
    for a, b in zip(x, y):  
        plt.text(a, b, (round(a,2),round(b,2)),ha='center', va='bottom', fontsize=10)
        print("{{",round(a,3),",",round((1-a),3),"},","{",round(b,3),",",round((1-b),3),"}}")
    plt.show()
    
#Specific For Coordination Game
CoordinationFunction(0,0,-1,4,4,-1,-2,-2)
