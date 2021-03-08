
# Ballistic Simulator with drag to calculate initial conditions to get a ball to desired
# x-coordinate if initial velocity is fixed
import math
import time


# Ballistic equations
#Initial Conditions
desi_distance = float(input("Desired Distance: "))
g = 9.81
vel_0 = 10



def calc_distance(vel_0, theta):
    theta_t = .1
    U_0 = vel_0*math.cos(math.radians(theta))
    V_0 = vel_0*math.sin(math.radians(theta))
    t = 2*V_0/g
    x = U_0*t
    return x

max_distance = calc_distance(vel_0, 45)

def find_target(curr_distance, theta):

    print(curr_distance)
    if desi_distance > max_distance:
        raise ValueError('Desired distance exceeds maximum distannce possible by out inadequate cannon')
    elif  desi_distance - .01 <= curr_distance <= desi_distance + .01:
        print("\nTheta: " + str(theta) + " deg" + "\nDistance: " + str(curr_distance) + " m" + "\nDesired Distance: " + str(desi_distance) + " m")
        return theta
    else:
       curr_distance = calc_distance(vel_0, theta)
       
       find_target(curr_distance, theta + .05)
      
       
    


find_target(0 , 45)

