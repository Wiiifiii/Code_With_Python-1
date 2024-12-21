"""
Task: Circular Motion Simulation (M03)

This script simulates a point moving in a circular path using the fourth-order Runge-Kutta method (RK4). The script writes the (x, y) coordinates of the point at each time step to a file named 'output.txt':
    t_i = Time instance, starting at 0 and ending at n*Dt.
    x_i = x-coordinate at time t_i.
    y_i = y-coordinate at time t_i.
Columns are separated by spaces, and the file contains n+1 lines, one for each time step including the initial condition.

Parameters:
    Dt = Time step for the simulation.
    n = Number of time steps to simulate.

The script utilizes RK4 to compute the position of the point at each time step based on its velocity and acceleration.
"""

import os
import numpy as np

# Output file path
filename = os.path.join(os.path.dirname(__file__), 'output.txt')

def rk_circle(dt, N):
    t = 0.0  # Initial time
    x = np.array([1.0, 0.0])  # Initial position in x and y

    def f(t, x):
        # Function representing the system of differential equations
        return np.array([-np.sin(t), np.cos(t)], dtype=np.float64)

    with open(filename, 'w') as file:
        file.write(f"{t:.6f} {x[0]:.6f} {x[1]:.6f}\n")  # Write initial condition

        for _ in range(1, N + 1):
            k1 = f(t, x)
            k2 = f(t + 0.5 * dt, x + 0.5 * dt * k1)
            k3 = f(t + 0.5 * dt, x + 0.5 * dt * k2)
            k4 = f(t + dt, x + dt * k3)
            x += dt * (k1 + 2*k2 + 2*k3 + k4) / 6  # Update position using RK4 formula
            t += dt  # Increment time
            file.write(f"{t:.6f} {x[0]:.6f} {x[1]:.6f}\n")  # Write new position to file

# Dt and N can be modified as needed
if __name__ == '__main__':
    import pandas as pd
    from matplotlib import pyplot as plt

    T = 19
    dt = 0.01
    N = int(T / dt)

    rk_circle(dt, N)
    data = pd.read_csv(filename, delimiter=' ', names=['t', 'x', 'y'])

    # Example to visualize the output
    if True:
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')
        plt.legend()
        plt.show()
        
# if __name__=='__main__':
#     import pandas as pd

#     T=19
#     dt=0.01
#     N=int(T/dt)

#     rk_circle(dt, N)
#     data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

#     accurate_values=np.array([[3.3, np.cos(3.3), np.sin(3.3)],
#                               [6.3, np.cos(6.3), np.sin(6.3)],
#                               [18.9, np.cos(18.9), np.sin(18.9)]])

#     assert len(data)==N+1, 'length of data error'
#     assert len(data.columns)==3, 'columns number error'

#     eps=0.01
#     assert abs(data['t'].min()-0)<eps
#     assert abs(data['t'].max()-N*dt)<eps

#     def compare_xy(data, t, x, y):
#         d=data.loc[(t-dt/2<data['t']) & (data['t']<t+dt/2)]
#         data_x=float(d['x'].iloc[0])
#         data_y=float(d['y'].iloc[0])
       
#         return abs(data_x-x), abs(data_y-y)
    
#     for t, x, y in accurate_values:
#         dx,dy=compare_xy(data, t, x, y)
#         assert dx<eps, "Accuracy error!"
#         assert dy<eps, "Accuracy error!"