"""
Task: Euler's Spiral Simulation (M02)

This script simulates a point moving in a spiral path using Euler's method. The velocity
and acceleration are determined by the given functions:
    v(0) = [0]
           [1]
    a(x) = (-1.25/||x||)*x - 0.3*v

The function euler_spiral(Dt, n) writes the (x, y) coordinates of the point at each time step to a file named 'output.txt':
    t_i = The time instance, starting at 0 and ending at n*Dt.
    x_i = The x-coordinate at time t_i.
    y_i = The y-coordinate at time t_i.
Columns are separated by spaces, and the file includes n+1 lines corresponding to each time step including the initial condition.

Parameters:
    Dt = Time step for the simulation.
    n = Number of time steps to simulate.

The simulation utilizes the Euler method to advance the position and velocity of the point at each step.
"""

import os
import numpy as np 

# Output file path
filename = os.path.dirname(__file__) + '/output.txt' 

def acceleration(x, v):
    # Calculate the norm of position vector x for use in acceleration formula
    norm_x = np.linalg.norm(x)
    if norm_x == 0:
        return -0.3 * v  # Only velocity-dependent damping if at the origin
    return (-1.25 / norm_x) * x - 0.3 * v  # Full acceleration formula

def euler_spiral(Dt, n):
    t = 0.0  # Start time
    x = np.array([1.0, 0.0])  # Initial position [1,0]
    v = np.array([0.0, 1.0])  # Initial velocity [0,1]

    with open(filename, 'w') as file:
        file.write(f"{t:.6f} {x[0]:.6f} {x[1]:.6f}\n")  # Write initial condition
        for _ in range(1, n + 1):
            a = acceleration(x, v)  # Calculate acceleration
            x += Dt * v  # Update position using current velocity
            v += Dt * a  # Update velocity using calculated acceleration
            t += Dt  # Increment time
            file.write(f"{t:.6f} {x[0]:.6f} {x[1]:.6f}\n")  # Write current time and position
# Dt and N can modify as needed.
# Dt = 0.01  # Time step
# n = 100    # Number of steps
# euler_spiral(Dt, n) # Call the function to write to file.

if __name__=='__main__':
    import pandas as pd
    from matplotlib import pyplot as plt 

    show_figure=True

    if show_figure:
        N=100
        dt=10/N
        euler_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        N=1000
        dt=10/N
        euler_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        N=10000
        dt=10/N
        euler_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        plt.legend()
        plt.show()

    N=100
    dt=10/N
    euler_spiral(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

    inaccurate_values=np.array([[4.3, 0.3307126723997306, -0.496816941228279],
                                 [6.7, -0.430393300335996, 0.310510067561188]])
    
    accurate_values=np.array([[4.3, 0.3370698183736534, -0.0921844565121777],
                              [6.3, -0.2046270799813872, -0.125834329656545]])

    assert len(data)==N+1, 'length of data error'
    assert len(data.columns)==3, 'columns number error'

    eps=0.0001
    assert abs(data['t'].min()-0)<eps
    assert abs(data['t'].max()-N*dt)<eps

    def compare_xy(data, t, x, y):
        d=data.loc[(t-eps<data['t']) & (data['t']<t+eps)]
        dx=float(d['x'])
        dy=float(d['y'])
       
        return abs(dx-x), abs(dy-y)
    
    for t, x, y in inaccurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps
        assert dy<eps

    N=10000
    dt=10/N
    euler_spiral(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
    for t, x, y in accurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps
        assert dy<eps
