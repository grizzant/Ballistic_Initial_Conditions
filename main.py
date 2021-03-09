
# Ballistic Simulator with drag to calculate initial conditions to get a ball to desired
# x-coordinate if initial velocity is fixed
import math
import sys 
import matplotlib.pyplot as plt
import numpy as np

  
  
sys.setrecursionlimit(10**6)


# Ballistic equations
#Initial Conditions
desi_distance = 5
g = 9.81
vel_0 = 10





def calc_distance(vel_0, theta):
    U_0 = vel_0*math.cos(math.radians(theta))
    V_0 = vel_0*math.sin(math.radians(theta))
    t = 2*V_0/g
    x = U_0*t
    return x

max_distance = calc_distance(vel_0, 45)
max_height = .5*vel_0**2/g


def find_target(curr_distance, theta):
    if desi_distance > max_distance:
        raise ValueError('Desired distance exceeds maximum distannce possible by out inadequate cannon')
    elif  desi_distance - .001 <= curr_distance <= desi_distance + .001:
        print("\nTheta: " + str(theta) + " deg" + "\nDistance: " + str(curr_distance) + " m" + "\nDesired Distance: " + str(desi_distance) + " m")
        return theta
        plt.show()
    else:
        
        curr_distance = calc_distance(vel_0, theta)
        graph_trajectory(round(theta), vel_0)
        find_target(curr_distance, theta + .05)
       
       
def graph_trajectory(theta, v_0):
    x = np.linspace(0, max_distance, num=100)
    y = x*math.tan(math.radians(theta))-((g*x**2)/(2*v_0**2*math.cos(math.radians(theta))**2))
    
    plt.plot(x,y)
    plt.xlim(0, max_distance+.1*max_distance)
    plt.ylim(0, max_height+.1*max_height)
    
       
    


find_target(0 , 45)

