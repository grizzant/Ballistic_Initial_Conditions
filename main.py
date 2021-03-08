
# Ballistic Simulator with drag to calculate initial conditions to get a ball to desired
# x-coordinate if initial velocity is fixed
import math
import time
import numpy as np
from scipy.integrate import solve_ivp





# Drag coefficient, projectile radius (m), area (m2) and mass (kg).
c = 0.47
r = 0.05
A = np.pi * r**2
m = 0.2
# Air density (kg.m-3), acceleration due to gravity (m.s-2).
rho_air = 1.28
g = 9.81
# For convenience, define  this constant.
k = 0.5 * c * rho_air * A

# Initial speed and launch angle (from the horizontal).
v0 = 50
phi0 = np.radians(65)

def deriv(t, u):
    x, xdot, z, zdot = u
    speed = np.hypot(xdot, zdot)
    xdotdot = -k/m * speed * xdot
    zdotdot = -k/m * speed * zdot - g
    return xdot, xdotdot, zdot, zdotdot

# Initial conditions: x0, v0_x, z0, v0_z.
u0 = 0, v0 * np.cos(phi0), 0., v0 * np.sin(phi0)
# Integrate up to tf unless we hit the target sooner.
t0, tf = 0, 50

def hit_target(t, u):
    # We've hit the target if the z-coordinate is 0.
    return u[2]
# Stop the integration when we hit the target.
hit_target.terminal = True
# We must be moving downwards (don't stop before we begin moving upwards!)
hit_target.direction = -1

def max_height(t, u):
    # The maximum height is obtained when the z-velocity is zero.
    return u[3]

soln = solve_ivp(deriv, (t0, tf), u0, dense_output=True,
                 events=(hit_target, max_height))






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

