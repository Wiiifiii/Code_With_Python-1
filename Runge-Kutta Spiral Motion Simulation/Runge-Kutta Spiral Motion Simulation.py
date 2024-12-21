"""
Task: Runge-Kutta Spiral Motion Simulation (M04)

This script simulates the motion of a particle under a specific force field using the fourth-order Runge-Kutta method (RK4). It writes the (x, y) coordinates of the particle at each time step to a file named 'output.txt':
    t_i = Time instance, starting at 0 and ending at n*Dt.
    x_i = x-coordinate at time t_i.
    y_i = y-coordinate at time t_i.
Columns are separated by spaces, and the file contains n+1 lines, one for each time step including the initial condition.

Parameters:
    Dt = Time step for the simulation.
    n = Number of time steps to simulate.

This script uses RK4 to compute the trajectory of the particle based on its dynamics dictated by the given force field.
"""

import os
import numpy as np 
# the output file path
filename=os.path.dirname(__file__)+'/output.txt'

# Function to calculate acceleration based on position and velocity.
def save(outf, x, t):
    """Writes the current time and position (x and y coordinates) to the file."""
    x_i = x[0]
    y_i = x[1]
    outf.write(f'{t:.6f} {x_i:.6f} {y_i:.6f}\n') # Write the time, x, and y coordinates to the file.

def acceleration(x, v):
    """Calculates the acceleration based on the current position and velocity."""
    norm_x = np.linalg.norm(x) # Compute the norm of the position vector x.
    if norm_x == 0: # Handle the case where the norm is zero to avoid division by zero.
        return -0.3 * v
    else:
        return (-1.25 / norm_x) * x - 0.3 * v # Return the acceleration vector.

def rk_step(x, v, dt):
    """Performs a single step of the RK4 integration method."""
    k1_x = v
    k1_v = acceleration(x, v) # Compute the initial k values for position and velocity.
    
    k2_x = v + 0.5 * dt * k1_v
    k2_v = acceleration(x + 0.5 * dt * k1_x, v + 0.5 * dt * k1_v) # Compute the intermediate k update values.
    
    k3_x = v + 0.5 * dt * k2_v
    k3_v = acceleration(x + 0.5 * dt * k2_x, v + 0.5 * dt * k2_v) # Compute the intermediate k next values.
    
    k4_x = v + dt * k3_v
    k4_v = acceleration(x + dt * k3_x, v + dt * k3_v) # Compute the final k values.
    
    x_next = x + (dt / 6) * (k1_x + 2*k2_x + 2*k3_x + k4_x) # Compute the next position and velocity.
    v_next = v + (dt / 6) * (k1_v + 2*k2_v + 2*k3_v + k4_v) # Using the weighted average of the k values.
    
    return x_next, v_next # Return the next position and velocity

def rk_spiral(Dt, n):
    """Simulates the motion using the RK4 method and writes the results to an output file."""
    t = 0.0 # Initial time
    x = np.array([1.0, 0.0]) # Initial position (x, y)
    v = np.array([0.0, 1.0]) # Initial velocity (v_x, v_y)
    with open(filename, 'w') as file: # Open the output file for writing
        for _ in range(n + 1): # Perform n + 1 iterations using _ as a throwaway variable.
            save(file, x, t) # Write the current time and position to the file
            t += Dt # Increment the time
            x, v = rk_step(x, v, Dt) # Perform a single RK4 step

    """ test code """
if __name__=='__main__':
    import pandas as pd
    from matplotlib import pyplot as plt 

    show_figure=False

    if show_figure:
        N=100
        dt=10/N
        rk_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        N=1000
        dt=10/N
        rk_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        N=10000
        dt=10/N
        rk_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        plt.legend()
        plt.show()

    N=100
    dt=10/N
    rk_spiral(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

    inaccurate_values=np.array([[4.3, 0.3359082477574567, -0.0883676533098237],
                                 [6.7, -0.0197869717386364, -0.2621124357821189]])
    
    accurate_values=np.array([[4.3, 0.335907484080501, -0.0883631123162162],
                              [6.3, -0.1992703282589062, -0.130683714199632]])

    assert len(data)==N+1, 'length of data error'
    assert len(data.columns)==3, 'columns number error'

    eps=0.0001
    assert abs(data['t'].min()-0)<eps
    assert abs(data['t'].max()-N*dt)<eps

    def compare_xy(data, t, x, y):
        d=data.loc[(t-eps<data['t']) & (data['t']<t+eps)]
        dx=float(d['x'].iloc[0])
        dy=float(d['y'].iloc[0])
        return abs(dx-x), abs(dy-y)
    
    for t, x, y in inaccurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps
        assert dy<eps

    N=10000
    dt=10/N
    rk_spiral(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
    for t, x, y in accurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps
        assert dy<eps
