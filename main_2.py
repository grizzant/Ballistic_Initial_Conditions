
# Ballistic Simulator with drag to calculate initial conditions to get a ball to desired
# x-coordinate if initial velocity is fixed
import math
import matplotlib.pyplot as plt
import numpy as np
  



# Ballistic equations
#Initial Conditions
desi_distance = 2
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
    elif  desi_distance - .01 <= curr_distance <= desi_distance + .01:
        print("\nTheta: " + str(theta) + " deg" + "\nDistance: " + str(curr_distance) + " m" + "\nDesired Distance: " + str(desi_distance) + " m")
        plt.show()
        return theta
    elif desi_distance > curr_distance:
       graph_trajectory(theta, vel_0)
       curr_distance = calc_distance(vel_0, theta)
       
       find_target(curr_distance, theta + .5*theta)
    elif desi_distance < curr_distance:
       graph_trajectory(theta, vel_0)
       curr_distance = calc_distance(vel_0, theta)
       
       find_target(curr_distance, theta - .5*theta) 
    else: 
        raise ValueError("Through find_target function, target not found!")
      
       
def graph_trajectory(theta, v_0):
    x = np.linspace(0, max_distance, num=30)
    y = x*math.tan(math.radians(theta))-((g*x**2)/(2*v_0**2*math.cos(math.radians(theta))**2))
    
    plt.plot(x,y)
    plt.xlim(0, max_distance+.1*max_distance)
    plt.ylim(0, max_height+.1*max_height)
    


find_target(0 , 22.5)

