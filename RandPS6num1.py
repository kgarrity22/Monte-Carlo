from pylab import*
import random

def monteCarlo():

#total number of points inside the intersection
    inside = 0
#total points we are generating
    totalPoints = 100000
#the volume of the box of intersection
    boxVol = 2*1*1

    x = 0 
    y = 0 
    z = 0


    for i in range(totalPoints):
        
        x = uniform(-1.0, 1.0)
        y = uniform(-0.5, 0.5)
        z = uniform(0.0, 1.0)

        

        # equations of the short cone
        shortcone1 = x**2 + y**2 #<=1
        shortcone2 = z #>= 0
        shortcone3 = 1 - (x**2+y**2)**0.5 #>= z

        # equations for the long cone
        longcone1 = (z - 0.5)**2 + y**2 # <= 0.25
        longcone2 = x #>= -2
        longcone3 = 2 - 8*(y**2 + (z - 0.5)**2)**0.5 #>= x

        if (shortcone1 <= 1 and 0 <= shortcone2 and shortcone2 <= shortcone3):
            if (longcone1 <= 0.25 and -2 <= longcone2 and longcone2 <= longcone3):
                inside = inside + 1
    print(inside)


    
    p = inside/totalPoints
    return (p * boxVol)

print(monteCarlo())
