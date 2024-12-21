"""
Task: Euler's Circle Simulation (M01)

This script simulates the motion of a point moving along a circular path using Euler's method. 
The velocity function v(t) is defined as:
    v(t) = [-sin(t)]
           [cos(t)]
and the initial position x(0) is at [1, 0] on the Cartesian plane.

The function euler_circle(Dt, n) writes the position coordinates (x, y) of the point at each time step to a file named output.txt. 
Each line in the file corresponds to a specific time from t=0 to t=n*Dt, where Dt is the time step and n is the number of steps.

Arguments:
    Dt (float): The time step for the simulation.
    n (int): The number of time steps to simulate.

The output file 'output.txt' will contain:
    t_i: The time instance, starting at 0 and ending at n*Dt.
    x_i: The x-coordinate at time t_i.
    y_i: The y-coordinate at time t_i.
Columns are separated by spaces, and the file includes n+1 lines corresponding to each time step including the initial condition.

The simulation uses the Euler method as described in the lecture slides.
"""

import numpy as np
import os

filename = os.path.dirname(__file__) + '/output.txt'  # Path to the output file

def f(t, x):
    # Function to return the velocity vector at time t for position x
    # Here, x[0] corresponds to the x-coordinate, x[1] to the y-coordinate
    return np.array([-np.sin(t), np.cos(t)], dtype=np.float64)

def euler_circle(dt, N):
    t = 0.0  # Starting time
    x = np.array([1.0, 0.0], dtype=np.float64)  # Initial position at (1,0) with type float64
    
    with open(filename, 'w') as file:
        for _ in range(N + 1):
            file.write(f"{t:.6f} {x[0]:.6f} {x[1]:.6f}\n")  # Writing time and coordinates to file
            t += dt  # Increment time by dt
            x += dt * f(t, x)  # Euler's method to update position

# Uncomment the following to test the function with custom parameters
# if __name__ == "__main__":
#     euler_circle(0.01, 100)

if __name__=='__main__':
    import pandas as pd

    T = 19  # Total simulation time
    dt = 0.001  # Time step size
    N = int(T / dt)  # Compute the number of steps

    euler_circle(dt, N)
    data = pd.read_csv(filename, delimiter=' ', names=['t', 'x', 'y'])

    # Example test values to validate the accuracy
    accurate_values = np.array([
        [3.3, np.cos(3.3), np.sin(3.3)],
        [6.3, np.cos(6.3), np.sin(6.3)],
        [18.9, np.cos(18.9), np.sin(18.9)]
    ])

    assert len(data) == N + 1, 'Length of data error'
    assert len(data.columns) == 3, 'Columns number error'

    eps = 0.001  # Precision threshold

    def compare_xy(data, t, x, y):
        # Function to compare computed and expected values within allowed precision
        d = data.loc[(t - dt / 2 < data['t']) & (data['t'] < t + dt / 2)]
        data_x = float(d['x'].iloc[0])
        data_y = float(d['y'].iloc[0])
        
        return abs(data_x - x), abs(data_y - y)

    for t, x, y in accurate_values:
        dx, dy = compare_xy(data, t, x, y)
        assert dx < eps, "Accuracy error"
        assert dy < eps, "Accuracy error"
